class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        an=[x for x in arr if arr.count(x)==1]
        return an[k-1] if k<=len(an) else ""