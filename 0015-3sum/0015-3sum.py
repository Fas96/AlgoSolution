class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for I in range(len(nums)):
            if I > 0 and nums[I] == nums[I-1]:
                continue
            L = I + 1
            R = len(nums)-1
            while L < R:
                threeSum = nums[I] + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([nums[I], nums[L], nums[R]])
                    L += 1
                    while nums[L]==nums[L-1] and L < R:
                        L += 1
                    
        return res
        