class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        n = len(nums)
        
        for i in range(n):
            mp[nums[i] - i] += 1
        
        good_pairs = sum((count * (count - 1)) // 2 for count in mp.values())
        
        return (n * (n - 1) // 2) - good_pairs