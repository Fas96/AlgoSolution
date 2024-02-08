class Solution:
    def numSquares(self, n: int) -> int:
        def backtrack(i, target, currLen, minLen):
            # found one solution
            if target == 0:
                return min(minLen, currLen)
            
            # return minLen if can't find a solution
            if i < 1 or currLen >= minLen:
                return minLen

            # try to find possible max number
            if i**2 <= target:
                minLen = backtrack(i, target - i**2, currLen + 1, minLen)
      
            minLen = backtrack(i-1, target, currLen, minLen)
            return minLen

        return backtrack(int(math.sqrt(n)), n, 0, float('inf'))