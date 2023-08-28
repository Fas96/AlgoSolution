class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        count = 0

        for i in range(1, len(s) + 1):
            count += 1
            if not (set(s[:i]).intersection(set(s[i:]))):
                res.append(count)
                count = 0
        return res
            
            
        