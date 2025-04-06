class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        self.res = []
        self.mem = [-1] * len(nums)
        self.helper(nums, 0, [], 1)
        return self.res
    
    def helper(self, nums, index, curr, prev):
        if len(curr) > len(self.res):
            self.res = curr[:]
        
        for i in range(index, len(nums)):
            if len(curr) > self.mem[i] and nums[i] % prev == 0:
                self.mem[i] = len(curr)
                curr.append(nums[i])
                self.helper(nums, i + 1, curr, nums[i])
                curr.pop()