class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        prev = 0
        while True:
            idx = bisect.bisect(nums, k, prev)
            if idx > prev:
                k += idx-prev
                prev = idx
            else:
                break
        return (1+k) * k // 2 - sum(nums[:prev])
        