# 📡 Agentic-Based Reinforcement Learning Framework for URLLC-Aware 5G Network Slicing Optimization

---

## Overview

This project extends an existing reinforcement learning-based network slicing environment by introducing an **Agentic RL framework** with **URLLC-aware optimization**.

It is based on the original work:

> *Model-Based Reinforcement Learning with Kernels for Resource Allocation in RAN Slices* (IEEE TWC 2023)

---

## 📖 Base Work (Original System)

The original repository provides:

- A **5G network slicing simulation environment**
- OpenAI Gym-based interface for RL agents
- Resource allocation across multiple slices:
  - eMBB (enhanced Mobile Broadband)
  - mMTC (massive Machine Type Communication)

### Algorithms Included:
- KBRL (Kernel-Based Reinforcement Learning)
- DQN (Deep Q-Network)
- NAF (Normalized Advantage Function)

### Objective:
Efficient allocation of **Physical Resource Blocks (PRBs)** while satisfying **Service Level Agreements (SLAs)**.

---

## My Contributions (Enhancements)

This project significantly extends the original system with the following improvements:

### Agentic Reinforcement Learning
- Designed an **agent-based decision-making system**
- Enabled dynamic and intelligent resource allocation

### 📶 URLLC-Aware Optimization
- Added **URLLC slice support**
- Modeled:
  - Ultra-low latency constraints
  - High reliability requirements

### 🤖 PPO Implementation
- Integrated **Proximal Policy Optimization (PPO)**
- Improved stability and adaptability of learning

### Custom Reward Function
- Designed reward based on:
  - SLA satisfaction
  - Latency minimization
  - Resource efficiency

### 📊 Performance Improvements
- Reduced SLA violations
- Improved PRB utilization
- Better adaptability under dynamic traffic conditions

---

## System Architecture

The system follows an **Agent–Environment interaction loop**:

1. Environment provides:
   - Traffic demand per slice
   - Available PRBs
   - SLA requirements  

2. Agent:
   - Observes system state  
   - Allocates PRBs using PPO policy  

3. Environment:
   - Executes allocation  
   - Returns reward based on SLA + efficiency  

4. Agent:
   - Updates policy iteratively  

---

## ⚙️ Installation & Setup

### Requirements
gym==0.15.3
numpy==1.19.1
pandas==0.25.2
stable-baselines==2.10.1
tensorflow==1.9.0
scipy==1.5.4
matplotlib==3.3.4



### Installation Steps

```bash
git clone https://github.com/Pawan41/Agentic-Based-Reinforcement-Learning-Framework-for-URLLC-Aware-5G-Network-Slicing-Optimization
cd gym-ran_slice
pip install -e .
```

### Experiments

Scripts available:

- experiments_rl.py → RL agents (PPO, DQN)
- experiments_kbrl.py → KBRL algorithm
- experiments_naf.py → NAF agent
- experiment_dqn.py → DQN agent

## Results

### Key Observations:
- ✅ URLLC slice achieves lower SLA violations
- ✅ Better latency-aware allocation
- ✅ Improved PRB efficiency



## Project Structure

### Environment
- node_b.py
- slice_ran.py
- slice_l1.py
- channel_models.py
- traffic_generators.py
- schedulers.py
- gym_ran_slice/ran_slice.py

  
### Algorithms
- kbrl_control.py
- algorithms/kernel.py
- algorithms/projectron.py

  
Custom Enhancements (My Work)
- PPO integration
- URLLC slice logic
- Modified reward function
- Agentic workflow implementation


### References
- Alcaraz et al., Model-Based Reinforcement Learning with Kernels for Resource Allocation in RAN Slices, IEEE TWC 2023
- OpenAI Gym
- Stable-Baselines
