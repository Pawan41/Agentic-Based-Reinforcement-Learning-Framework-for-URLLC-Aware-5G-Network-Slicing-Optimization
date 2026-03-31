"""
Created on Friday March 2026

@author: Pawan Kumar

"""


import numpy as np

class URLLC_UE:
    def __init__(self, id, slice_ran_id):
        self.id = id

        # required by scheduler
        self.repetitions = 1

        self.slice_ran_id = slice_ran_id

class SliceRANURLLC:

    def __init__(self, rng, id):
        self.rng = rng
        self.id = id
        self.info = {}
        self.type = "urllc"

        # SLA requirements
        self.delay_requirement = 1   # ms
        self.reliability = 0.9999

        self.reset()

    def reset(self):
        self.delay = 0
        self.packet_loss = 0
        self.traffic = self.rng.integers(5, 15)

    def reset_info(self):
        pass

    def get_state(self):
        return np.array([self.delay, self.traffic], dtype=float)

    def get_n_variables(self):
        return 2

    def slot(self):

        # number of new URLLC packets
        n_arrivals = self.rng.integers(1, 3)

        arrivals = [URLLC_UE(self.rng.integers(1000, 9999), self.id) for _ in range(n_arrivals)]

        # simulate departures
        n_departures = self.rng.integers(0, len(arrivals)+1)
        departures = arrivals[:n_departures]

        # FIXED delay update
        self.delay = max(0, self.delay + len(arrivals) - len(departures))
        
        self.info = {
            'delay': self.delay,
            'traffic': self.traffic
        }

        return arrivals, departures

    def update_info(self, delay, avg_rep, devices):
        self.delay = delay

    def compute_reward(self):
        if self.delay > self.delay_requirement:
            return 1   # one violation
        else:
            return 0   # no violation