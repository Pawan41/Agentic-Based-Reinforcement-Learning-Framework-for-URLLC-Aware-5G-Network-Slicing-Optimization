"""

@author: Pawan Kumar

"""

import numpy as np


class RulePolicyAgent:

    def __init__(self, n_slices, total_prbs=100):

        self.n_slices = n_slices
        self.total_prbs = total_prbs
        self.metrics = None

    def observe(self, metrics):
        """
        metrics expected format:
        [
            {"delay": value, "queue": value},
            ...
        ]
        """
        self.metrics = metrics

    def decide(self):

        if self.metrics is None:
            return np.ones(self.n_slices) * (self.total_prbs // self.n_slices)

        delays = []
        queues = []

        for m in self.metrics:
            delays.append(m.get("delay", 1))
            queues.append(m.get("queue", 1))

        delays = np.array(delays)
        queues = np.array(queues)

        # normalize metrics
        delays = delays / (delays.sum() + 1e-6)
        queues = queues / (queues.sum() + 1e-6)

        # combine delay + queue pressure
        priority = 0.6 * delays + 0.4 * queues

        priority = priority / priority.sum()

        prb_allocation = (priority * self.total_prbs).astype(int)

        # ensure at least 1 PRB per slice
        prb_allocation[prb_allocation == 0] = 1

        return prb_allocation