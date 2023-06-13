class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return  max(Counter(nums).values()) > 1
        # return len(set(nums))!=len(nums)
            
        