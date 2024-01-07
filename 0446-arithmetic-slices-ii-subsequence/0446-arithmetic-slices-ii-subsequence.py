class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cnt = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                delta = nums[i] - nums[j]
                if delta < -2**31 or delta > 2**31 - 1:
                    continue
                diff = int(delta)
                sum_val = cnt[j][diff]
                origin = cnt[i][diff]
                cnt[i][diff] = origin + sum_val + 1
                ans += sum_val

        return int(ans)