class Solution:
    def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        @functools.lru_cache(None)
        def dfs(xcurr, ycurr, k):
            if xcurr < 0 or xcurr >= n or ycurr < 0 or ycurr >= n:
                return 0
            elif k == 0: 
                return 1
            else: 
                return (dfs(xcurr + 2, ycurr + 1, k - 1) + 
                        dfs(xcurr + 1, ycurr + 2, k - 1) + 
                        dfs(xcurr - 1, ycurr + 2, k - 1) + 
                        dfs(xcurr - 2, ycurr + 1, k - 1) + 
                        dfs(xcurr - 2, ycurr - 1, k - 1) + 
                        dfs(xcurr - 1, ycurr - 2, k - 1) + 
                        dfs(xcurr + 1, ycurr - 2, k - 1) +   
                        dfs(xcurr + 2, ycurr - 1, k - 1)) / 8

        return dfs(r, c, k)
        