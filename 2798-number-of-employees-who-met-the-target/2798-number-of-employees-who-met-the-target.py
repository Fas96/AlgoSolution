class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        nums=hours
        return sum(x>=target for x in nums)
        