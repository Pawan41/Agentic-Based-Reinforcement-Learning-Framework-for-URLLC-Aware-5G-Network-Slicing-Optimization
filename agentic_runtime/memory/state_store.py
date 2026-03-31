class StateStore:

    def __init__(self):

        self.history = []

    def store(self, state, action, reward):

        record = {
            "state": state,
            "action": action,
            "reward": reward
        }

        self.history.append(record)

    def get_history(self):

        return self.history