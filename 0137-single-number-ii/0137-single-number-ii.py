class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = temp = 0
        
        for n in nums:
            ans=(ans ^ n)&  ~temp
            temp=(temp ^ n)& ~ans
        
        return ans
        