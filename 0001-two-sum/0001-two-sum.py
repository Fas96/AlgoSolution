class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L,R=0,len(nums)
        while L<R:
            go=L+1
            while  go< R:
                if nums[L]+nums[go]==target:
                    return [L,go]
                go+=1
            L+=1
        return [-1,-1]