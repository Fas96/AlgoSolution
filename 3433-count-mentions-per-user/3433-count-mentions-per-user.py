from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        by_time = {}
        for ev in events:
            t = int(ev[1])
            by_time.setdefault(t, []).append(ev)

        mentions = [0] * numberOfUsers
        is_online = [True] * numberOfUsers
        offline_until = [0] * numberOfUsers

        for t in sorted(by_time.keys()):
            evs = by_time[t]

            for i in range(numberOfUsers):
                if not is_online[i] and offline_until[i] <= t:
                    is_online[i] = True
                    offline_until[i] = 0

            for ev in evs:
                if ev[0] == "OFFLINE":
                    id_ = int(ev[2])
                    is_online[id_] = False
                    offline_until[id_] = t + 60

            for ev in evs:
                if ev[0] != "MESSAGE":
                    continue
                tokens = ev[2].split()
                for token in tokens:
                    if token == "ALL":
                        for i in range(numberOfUsers):
                            mentions[i] += 1
                    elif token == "HERE":
                        for i in range(numberOfUsers):
                            if is_online[i]:
                                mentions[i] += 1
                    elif token.startswith("id"):
                        id_ = int(token[2:])
                        if 0 <= id_ < numberOfUsers:
                            mentions[id_] += 1

        return mentions