class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before, after = [], []  
        for num in nums:  
            if num < pivot:
                before.append(num)
            elif num > pivot:
                after.append(num)

        equal_pivot = len(nums) - len(before) - len(after)  
        return before + [pivot] * equal_pivot + after  