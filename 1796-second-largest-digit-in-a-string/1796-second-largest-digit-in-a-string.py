class Solution:
    def secondHighest(self, s: str) -> int:
        numList = list()
        for ch in set(s):
            if ch.isnumeric():
                numList.append(ch)
        numList.sort()
        if len(numList) < 2:
            return -1
        return numList[len(numList) - 2]