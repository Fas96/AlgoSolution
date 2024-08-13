class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(candidates: List[int], index: int, target: int, el: List[int] ):
            if target < 0: return
            if target == 0:
                result.append(list(el))
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]: continue
                el.append(candidates[i])
                dfs(candidates, i + 1, target - candidates[i], el)
                el.pop()
        dfs(candidates, 0, target, [])
        return result
    
    