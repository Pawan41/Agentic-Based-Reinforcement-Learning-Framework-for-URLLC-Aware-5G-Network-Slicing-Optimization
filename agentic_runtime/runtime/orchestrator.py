import numpy as np
import csv

class Orchestrator:

    def __init__(self, simulator,
                 monitor,
                 policy,
                 rl_agent,
                 merger,
                 reflection,
                 memory):

        self.simulator = simulator
        self.monitor = monitor
        self.policy = policy
        self.rl_agent = rl_agent
        self.merger = merger
        self.reflection = reflection
        self.memory = memory

        # detect number of slices from env
        self.n_slices = simulator.env.n_slices

    def run_episode(self, max_steps=100):

        state = self.simulator.reset()

        info = None
        log_data = []

        for step in range(max_steps):

            metrics = self.monitor.observe(state, info)

            self.policy.observe(metrics)
            rule_action = self.policy.decide()

            self.rl_agent.observe(state)
            rl_action = self.rl_agent.decide()

            print("Rule action:", rule_action)
            print("RL action:", rl_action)

            action = self.merger.merge(rule_action, rl_action)
        
            action = np.array(action)
            
            # URLLC PRIORITY FIX
            urllc_index = -1

            # Adaptive Allocation
            if step > 0 and reward < 0:
                action[urllc_index] += 5
            else:
                action[urllc_index] = max(action[urllc_index], 20)

            if action.size != self.n_slices:
                action = np.ones(self.n_slices) * (self.simulator.env.n_prbs // self.n_slices)

            # ADD New Code 
            action = action.astype(float)

            total_prbs = self.simulator.env.n_prbs

            if action.sum() > total_prbs:
                action = action * (total_prbs / action.sum())

            action = action.astype(int)
            
            # Ensure URLLC priority
            urllc_index = -1
            action[urllc_index] = max(action[urllc_index], 15)

            print("Action:", action, "Sum:", action.sum())
            
            # ADD New Code 
            print("URLLC PRB:", action[-1])

            next_state, reward, done, info = self.simulator.step(action)

            prb_used = action.sum()

            log_data.append({
                "step": step,
                "reward": reward,
                "prb_used": prb_used
            })

            self.memory.store(state, action, reward)

            self.reflection.evaluate(state, action, next_state, reward)

            state = next_state

            if done:
                break

        # Save experiment results
        with open("simulation_results.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["step", "reward", "prb_used"])
            writer.writeheader()
            writer.writerows(log_data)