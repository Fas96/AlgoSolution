class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        c = collections.Counter(nums)
        mx = 0
        mxi = 0
        for k in c.keys():
            if c[k] > mx:
                mx = c[k]
                mxi = k

        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] += prefix[i]
            if nums[i] == mxi:
                prefix[i + 1] += 1

        for i in range(1, N):
            if prefix[i] * 2 > i and (prefix[N] - prefix[i]) * 2 > N - i:
                return i - 1
        return -1