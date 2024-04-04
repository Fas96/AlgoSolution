class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        fq=Counter(nums)
        if any(x>1 for x in fq.values() ): return False
        mx,mn=max(nums),min(nums)
        if mx-mn+1!=len(fq):return False
        return True
        