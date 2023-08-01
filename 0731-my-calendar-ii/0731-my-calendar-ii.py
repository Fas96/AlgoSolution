class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        # 3 overlaps
        overlaps = []
        for s, e in self.events:
            if s < end and start < e:
                overlaps.append((max(s, start), min(e, end)))
        # 2 overlaps
        for i in range(len(overlaps)):
            for j in range(i + 1, len(overlaps)):
                if overlaps[i][0] < overlaps[j][1] and overlaps[j][0] < overlaps[i][1]:
                    return False
        self.events.append((start, end))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)