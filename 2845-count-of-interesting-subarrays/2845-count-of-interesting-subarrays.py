class Solution:
    def countInterestingSubarrays(self, nums: List[int], MOD: int, k: int) -> int:
        px = [0] * (len(nums))
        for i in range(len(nums)):
            px[i] = 1 if nums[i] % MOD == k else 0
        freq = Counter()
        cnt = 0
        tt = 0
        for x in px:
            tt += x
            if tt % MOD == k: cnt += 1
            nx = tt % MOD - k
            if nx < 0: nx += MOD
            cnt += freq[nx]
            freq[tt % MOD] += 1
        return cnt