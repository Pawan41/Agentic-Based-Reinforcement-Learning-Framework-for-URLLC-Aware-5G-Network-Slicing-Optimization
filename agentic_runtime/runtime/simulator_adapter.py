"""

@author: Pawan Kumar

"""

import sys
import os

# add project root to path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)

from scenario_creator import create_env


class SimulatorAdapter(object):

    def __init__(self):

        # random generator
        import numpy as np
        rng = np.random.default_rng(0)

        # create environment
        self.env = create_env(rng, n=1)

        self.state = None

    def reset(self):

        self.state = self.env.reset()
        return self.state

    def step(self, action):

        next_state, reward, done, info = self.env.step(action)

        self.state = next_state

        return next_state, reward, done, info