class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ps = 0
        count = 0
        sum_freq = {0: 1} 
        for num in nums:
            ps += num
            if ps - k in sum_freq:
                count += sum_freq[ps - k]
            sum_freq[ps] = sum_freq.get(ps, 0) + 1
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
        