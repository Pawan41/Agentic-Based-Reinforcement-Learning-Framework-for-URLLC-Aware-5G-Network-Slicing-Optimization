import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("simulation_results.csv")

plt.figure()
plt.plot(data["step"], data["reward"])
plt.title("Reward vs Step")
plt.xlabel("Step")
plt.ylabel("Reward")
plt.grid()
plt.show()

plt.figure()
plt.plot(data["step"], data["prb_used"])
plt.title("PRB Usage vs Step")
plt.xlabel("Step")
plt.ylabel("PRBs Used")
plt.grid()
plt.show()