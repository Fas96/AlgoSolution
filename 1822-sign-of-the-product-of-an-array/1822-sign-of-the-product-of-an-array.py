class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for n in nums:
            if n==0:
                ans*=0
            elif n > 0:
                ans*=1
            elif n<0:
                ans*=(-1)
        return ans
        