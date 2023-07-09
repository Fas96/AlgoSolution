class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0
        for x in "abcdefghijklmnopqrstuvwxyz":
            for y in "abcdefghijklmnopqrstuvwxyz":
                if x != y:
                    prefix = 0
                    buff = 0
                    m = 10000
                    for ch in s:
                        if ch == x:
                            prefix += 1
                        elif ch == y:
                            m = min(m, buff)
                            prefix-=1
                            buff = prefix
                        ans = max(ans, prefix - m)
        return ans
        