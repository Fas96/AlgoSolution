from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        
        def backtrack(index):
            if index == len(res):
                return True
            if res[index] != 0:
                return backtrack(index + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    res[index] = 1
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    res[index] = 0
                    used[num] = False
                elif index + num < len(res) and res[index + num] == 0:
                    res[index] = res[index + num] = num
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    res[index] = res[index + num] = 0
                    used[num] = False
            return False
        
        backtrack(0)
        return res
