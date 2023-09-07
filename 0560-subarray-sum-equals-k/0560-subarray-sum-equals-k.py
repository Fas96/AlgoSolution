class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        running_sum = 0
        count = 0
        sum_freq = {0: 1} 
        for num in nums:
            running_sum += num
            if running_sum - k in sum_freq:
                count += sum_freq[running_sum - k]
            sum_freq[running_sum] = sum_freq.get(running_sum, 0) + 1

        return count
#         c={}
#         @cache
#         def go(idx, cs):
#             if idx == len(nums):
#                 return 0
#             count = 0
#             if (idx,cs) in c:
#                 return c[(idx,cs)]
#             if cs + nums[idx] == k:
#                 count += 1
#             count += go(idx + 1, cs + nums[idx])
#             c[(idx,cs)]=count
#             return count

#         ttc = 0
#         for i in range(len(nums)):
#             ttc += go(i, 0)

#         return ttc
        