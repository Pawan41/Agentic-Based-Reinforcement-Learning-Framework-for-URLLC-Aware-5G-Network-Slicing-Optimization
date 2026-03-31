import numpy as np

class RLAgent:

    def __init__(self, n_slices):
        self.n_slices = n_slices

    def observe(self, state):
        self.state = state

    def decide(self):
        # random allocation for now
        return np.random.randint(5, 25, size=self.n_slices)