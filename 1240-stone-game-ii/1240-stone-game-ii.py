class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # Create a suffix sum array to store the sum of piles from i to end
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i]

        # Memoization table
        dp = {}

        def dfs(i, M):
            # If we're at the last pile, return all remaining stones
            if i == n:
                return 0
            # If the result is already computed, return it
            if (i, M) in dp:
                return dp[(i, M)]

            max_stones = 0
            # Try to take X piles, where 1 <= X <= 2M
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                # The opponent will try to minimize Alice's stones, so we minimize the result of the next move
                max_stones = max(max_stones, suffix_sum[i] - dfs(i + X, max(M, X)))

            dp[(i, M)] = max_stones
            return max_stones

        return dfs(0, 1)



        