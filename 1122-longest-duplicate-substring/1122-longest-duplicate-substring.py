class Solution:
    def longestDupSubstring(self, s: str) -> str:

        def calc(n):
            nonlocal ans
            if not n:
                return True
            visited = set()
            for i in range(len(s)-n+1):
                if s[i:i+n] in visited:
                    ans = s[i:i+n]
                    return True
                visited.add(s[i:i+n])
            return False

        l = 0
        h = len(s)-1
        ans = ''
        while l<=h:
            mid = (l+h)//2
            if calc(mid):
                l = mid+1
            else:
                h=mid-1
        return ans