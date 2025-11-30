class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        rm = total_sum % p
        if rm == 0: return 0
        cursm = 0
        res = len(nums)
        pm = {0: -1}
        for i in range(0, len(nums)):
            cursm +=nums[i] % p
            needMod = (cursm - rm + p) % p
            if needMod in pm:
                res = min(res, i - pm[needMod])
            pm[cursm % p] = i
        return res if res < len(nums) else -1