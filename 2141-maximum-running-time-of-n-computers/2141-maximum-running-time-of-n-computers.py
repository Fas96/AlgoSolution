class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def check(mid):
            return sum(min(mid, v) for v in batteries) >= n * mid
        
        low, high = 0, sum(batteries)//n
        while low < high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid
        
        return low if check(low) else low-1