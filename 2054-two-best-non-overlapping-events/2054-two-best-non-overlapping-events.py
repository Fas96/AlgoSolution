class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        first_event_end = [0]
        first_event_val = [0] # Best up to corresponding end time
        max_seen = 0
        for start, end, val in events:
            max_seen = max(max_seen, val)
            first_event_end.append(end)
            first_event_val.append(max_seen)

        events.sort(key=lambda x: x[0])
        cur = 0
        ans = 0

        for start, end, val in events:
            while first_event_end[cur + 1] < start:
                cur += 1
            ans = max(ans, val + first_event_val[cur])

        return ans