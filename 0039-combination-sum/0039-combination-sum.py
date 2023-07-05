class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or idx >= len(candidates):
                return
            dfs(idx + 1, cur, total)
            cur.append(candidates[idx])
            dfs(idx, cur, total + candidates[idx])
            cur.pop()

        dfs(0, [], 0)
        return res
        