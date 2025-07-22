class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        output = 0
        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        index = {nums[0]:0}
        start_index = 0
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
            if nums[i] in index and index[nums[i]] >= start_index:
                output = max(output, prefix_sum[i-1]-prefix_sum[start_index]+nums[start_index])
                start_index = index[nums[i]] + 1 
            index[nums[i]] = i
        return max(output, prefix_sum[-1] - prefix_sum[start_index] + nums[start_index])


        