class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        freq = Counter(x for i, x in enumerate(nums) if i and nums[i-1] == key)
        print(freq)
        return max(freq, key=freq.get)