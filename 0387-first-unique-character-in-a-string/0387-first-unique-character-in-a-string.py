class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp=Counter(s)
        for i,x in enumerate(s):
            if mp[x]==1:
                return i
        return -1
        