class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        f=sorted(set(arr))
        mp={num: rank + 1 for rank, num in enumerate(f)}
        return [mp[x] for x in arr]
        