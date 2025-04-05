class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def bk(nums, index, subset, subsets): 
            if index == len(nums):
                subsets.append(subset[:])
                return 
            subset.append(nums[index])
            bk(nums, index + 1, subset, subsets)
            subset.pop() 
            bk(nums, index + 1, subset, subsets)
 
        subsets = []
        bk(nums, 0, [], subsets)
        result = 0
        for subset in subsets:
            subset_XOR_total = 0
            for num in subset:
                subset_XOR_total ^= num
            result += subset_XOR_total

        return result 