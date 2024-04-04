class Solution:
    def romanToInt(self, s: str) -> int:
        mp={
            "I":             1,
            "V":             5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M" :            1000}
        nm,idx=0,0
        n=len(s)
        while idx <len(s):
            c=s[idx]
            if idx < n - 1 and mp[s[idx + 1]] > mp[c]:
                nm+=(mp[s[idx + 1]]-mp[c])
                idx+=2
                continue
            else:
                nm+=mp[c]
            idx+=1
        return nm
        