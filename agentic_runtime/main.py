from agents.monitor import MonitoringAgent
from agents.policy_rule import RulePolicyAgent
from agents.rl_agent import RLAgent
from agents.merger import MergerAgent
from agents.reflection import ReflectionAgent

from memory.state_store import StateStore

from runtime.simulator_adapter import SimulatorAdapter
from runtime.orchestrator import Orchestrator


def main():

    simulator = SimulatorAdapter()

    # detect number of slices
    n_slices = simulator.env.n_slices

    monitor = MonitoringAgent()
    policy = RulePolicyAgent(n_slices)
    rl_agent = RLAgent(n_slices)
    merger = MergerAgent(n_slices)
    reflection = ReflectionAgent()
    memory = StateStore()

    orchestrator = Orchestrator(
        simulator,
        monitor,
        policy,
        rl_agent,
        merger,
        reflection,
        memory
    )

    orchestrator.run_episode()


if __name__ == "__main__":
    main()