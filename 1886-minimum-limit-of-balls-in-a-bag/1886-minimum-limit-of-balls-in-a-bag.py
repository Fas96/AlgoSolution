class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canAchievePenalty(penalty):
            operations = 0
            for balls in nums:
                if balls > penalty:
                    operations += (balls - 1) // penalty
            return operations <= maxOperations
        
       
        left, right = 1, max(nums) 
        while left < right:
            mid = (left + right) // 2
            if canAchievePenalty(mid):
                right = mid 
            else:
                left = mid + 1 
        return left