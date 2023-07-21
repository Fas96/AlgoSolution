class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def lis(i): 
            if i < 0:  return (0, 0) 
            
            if i in cache: return cache[i]
 
            subseqences = [(0,1)]

            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]: subseqences.append(lis(j))
 
            longest = max(subseqences)[0]
 
            count = sum(i[1] for i in subseqences if i[0] == longest)
 
            cache[i] = (longest + 1, count)

            return (longest + 1, count)
 
        subseqences = [lis(i) for i in range(len(nums) - 1, -1, -1)]
 
        return sum(i[1] for i in subseqences if i[0] == max(subseqences)[0])
        