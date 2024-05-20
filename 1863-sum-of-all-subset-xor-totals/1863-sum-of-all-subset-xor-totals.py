from functools import reduce
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(arr, index, current, all_subsets):
            if index == len(arr):
                all_subsets.append(current[:])
                return
            current.append(arr[index])
            backtrack(arr, index + 1, current, all_subsets)
            current.pop()
            backtrack(arr, index + 1, current, all_subsets)

        def generateSubsets(arr):
            all_subsets = []
            backtrack(arr, 0, [], all_subsets)
            return all_subsets
        def findXOR(arr):
            return reduce(lambda x, y: x ^ y, arr)
        ans=0
         
        for x in generateSubsets(nums):
            if len(x)<=0:
                continue
            ans+=(findXOR(x))
        return ans
        
                
        