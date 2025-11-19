class Solution:
    def findFinalValue(self, nums: List[int], o: int) -> int:
        nums.sort()
        while True:
            idx=bisect.bisect_left(nums,o) 
            if idx>len(nums)-1 or nums[idx] != o:
                break
            o*=2
        return o