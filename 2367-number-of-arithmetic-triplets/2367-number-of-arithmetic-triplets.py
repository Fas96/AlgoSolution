class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int: 
        return sum(1 for x in nums if x + diff in nums and x + 2 * diff in nums)

        
        # ans = 0 
        # for x in nums:
        #     if x + diff in nums and x + 2 * diff in nums:
        #         ans += 1
        # return ans
        
        
       #nums[j] + nums[j]  ==  nums[k] * nums[i]