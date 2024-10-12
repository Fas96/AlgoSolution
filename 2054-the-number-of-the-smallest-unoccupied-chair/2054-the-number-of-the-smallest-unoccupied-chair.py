class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for ind, (start, end) in enumerate(times):
            events.append((start, ind, "start"))
            events.append((end, ind, "end"))
        events.sort(key=lambda x: (x[0], x[2] == 'start'))
        ac = list(range(len(times)))
        heapq.heapify(ac)
        occupy_chair = {}
        for start, frnd, event_type in events:
            if event_type == "start":
                chair = heapq.heappop(ac)
                occupy_chair[frnd] = chair
                if frnd == targetFriend:
                    return chair
            else:
                chair = occupy_chair[frnd]
                heapq.heappush(ac, chair)