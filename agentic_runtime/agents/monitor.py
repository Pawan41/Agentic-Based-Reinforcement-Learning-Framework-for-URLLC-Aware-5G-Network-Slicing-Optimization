class MonitoringAgent:

    def observe(self, state, info=None):

        metrics = []

        if info is None:
            return metrics

        l1_info = info.get("l1_info", [])

        for s in l1_info:

            slice_data = list(s.values())[0]

            metrics.append({
                "delay": slice_data.get("delay", 1),
                "queue": slice_data.get("cbr_queue", 1)
            })

        return metrics