class Solution:
    def maxSum(self, nums: List[int]) -> int:
        val=set(nums)  
        pos,neg=[],[]
        for g in val:
            if g>0:
                pos.append(g)
            else:
                neg.append(g)
        if len(pos)>0:
            return sum(pos)
        else:
            return max(neg)
        return 0
        