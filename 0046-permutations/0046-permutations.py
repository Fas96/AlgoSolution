class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(path):
            if len(path) == len(nums):
                ans.append(path)
                return
            for i in nums:
                if i not in path:
                    dfs(path + [i])
        dfs([])
        return ans
