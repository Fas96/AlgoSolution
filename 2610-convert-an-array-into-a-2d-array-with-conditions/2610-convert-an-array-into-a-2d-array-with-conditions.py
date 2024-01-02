class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        output = []

        while len(nums):
            output.append(list(set(nums)))
            for i in output[-1]:
                nums.pop(nums.index(i))
        
        return output
        