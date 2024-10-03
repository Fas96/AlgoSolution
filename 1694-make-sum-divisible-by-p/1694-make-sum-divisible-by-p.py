class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        if remainder == 0: return 0
        currSumMod = 0
        res = len(nums)
        prefix_map = {0: -1}
        for i in range(0, len(nums)):
            currSumMod +=nums[i] % p
            needMod = (currSumMod - remainder + p) % p

            if needMod in prefix_map:
                res = min(res, i - prefix_map[needMod])

            prefix_map[currSumMod % p] = i


        return res if res < len(nums) else -1
           