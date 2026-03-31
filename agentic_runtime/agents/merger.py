import numpy as np


class MergerAgent:

    def __init__(self, n_slices=2, total_prbs=50):
        self.n_slices = n_slices
        self.total_prbs = total_prbs

    def merge(self, rule_action, rl_action):

        merged = []

        for r, rl in zip(rule_action, rl_action):
            merged.append(int(0.7 * r + 0.3 * rl))

        # ensure correct size
        while len(merged) < self.n_slices:
            merged.append(self.total_prbs // self.n_slices)

        merged = merged[:self.n_slices]

        # clip values
        merged = np.clip(merged, 0, self.total_prbs)

        return merged.tolist()