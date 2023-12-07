class Solution:
    def largestOddNumber(self, s: str) -> str: 
        n = len(s)

        for i in range(n - 1, -1, -1):
            a = int(s[i])
            if a % 2 != 0:
                return s[:i + 1]

        return ""
        
        