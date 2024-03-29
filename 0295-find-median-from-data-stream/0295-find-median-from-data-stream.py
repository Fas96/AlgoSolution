class MedianFinder:

    def __init__(self):
        self.mnhp = [] 
        self.mxhp = []

    def addNum(self, num: int) -> None:
        if not self.mxhp or num <= -self.mxhp[0]:
            heappush(self.mxhp, -num)
        else:
            heappush(self.mnhp, num)
         
        if len(self.mxhp) > len(self.mnhp) + 1:
            heappush(self.mnhp, -heappop(self.mxhp))
        elif len(self.mnhp) > len(self.mxhp):
            heappush(self.mxhp, -heappop(self.mnhp))

    def findMedian(self) -> float:
        if len(self.mxhp) == len(self.mnhp):
            return (-self.mxhp[0] + self.mnhp[0]) / 2
        else:
            return -self.mxhp[0] 