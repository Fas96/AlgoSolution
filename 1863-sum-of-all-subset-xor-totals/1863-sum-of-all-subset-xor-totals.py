from functools import reduce
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(arr, index, current):
            if index == len(arr):
                return [current[:]]
            current.append(arr[index])
            subsets_with_current = backtrack(arr, index + 1, current)
            current.pop()
            subsets_without_current = backtrack(arr, index + 1, current)
            return subsets_with_current + subsets_without_current
 
        ans=0
        for x in backtrack(nums, 0, []):
            if len(x)<=0:
                continue
            ans+=(reduce(lambda x, y: x ^ y,x))
        return ans
        
                
        