class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        m = len(nums)
        freq = collections.Counter(nums)
        dominant = None
        for k, count in freq.items():
            if count * 2 > m:
                dominant = k
                break
        if dominant is None:
            return -1

        left, right = 0, freq[dominant]
        for i, a in enumerate(nums):
            if a == dominant:
                left += 1
                right -= 1
            if left * 2 > i + 1 and right * 2 > m - i - 1:
                return i
        return -1