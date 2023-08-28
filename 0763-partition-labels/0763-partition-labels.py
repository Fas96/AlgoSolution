class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i = 1
        count = 0
        res = []
        while (i <len(s)+1):
            count += 1 
            if not (set(s[:i]).intersection(set(s[i:]))): 
                res.append(count)
                count = 0
            i += 1
        return res
            
            
        