class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
     
        return generateSubsets(nums)
        