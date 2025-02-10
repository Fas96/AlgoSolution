class Solution:
    def clearDigits(self, s: str) -> str:
        res=""
        for c in s:
            if c.isnumeric():
                if res:
                    res=res[:-1]
            else:
                res+=c

        return res
            
            
        