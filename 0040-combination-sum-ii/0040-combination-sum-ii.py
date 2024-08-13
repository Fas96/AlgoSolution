class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.dfs(candidates, 0, target, [], result)
        return result
    
    def dfs(self, candidates: List[int], index: int, target: int, current_list: List[int], result: List[List[int]]):
        if target < 0: return
        if target == 0:
            result.append(list(current_list))
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]: continue
            current_list.append(candidates[i])
            self.dfs(candidates, i + 1, target - candidates[i], current_list, result)
            current_list.pop()