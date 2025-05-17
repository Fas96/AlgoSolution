class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx,count=0,Counter(nums)
        for color in range(3):
            freq = count.get(color, 0)
            nums[idx : idx + freq] = [color] * freq
            idx += freq