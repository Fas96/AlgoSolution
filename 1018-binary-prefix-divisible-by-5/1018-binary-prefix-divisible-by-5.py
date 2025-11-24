class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
    
        ans = []
        n = 0
        for num in nums:
            n = (n * 2 + num) % 5
            ans.append(n == 0)
        return ans