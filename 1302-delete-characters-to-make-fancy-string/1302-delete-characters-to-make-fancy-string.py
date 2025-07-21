class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        result = []
        for char in s:
            if len(result) >= 2 and result[-1] == result[-2] == char:
                continue
            result.append(char)
        
        return ''.join(result)
        