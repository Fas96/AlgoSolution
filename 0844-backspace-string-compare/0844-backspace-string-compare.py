class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        ss = tt = 0
        while 0 <= i or 0 <= j: 
            while 0 <= i and (s[i] == "#" or ss): 
                if s[i] == "#": ss += 1
                else: ss -= 1
                i -= 1
            while 0 <= j and (t[j] == "#" or tt): 
                if t[j] == "#": tt += 1
                else: tt -= 1
                j -= 1
            if i < 0 and 0 <= j or 0 <= i and j < 0 or 0 <= i and 0 <= j and s[i] != t[j]: return False 
            i, j = i-1, j-1
        return True 