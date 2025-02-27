class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hashmap = {num:i for  i , num in enumerate(arr)}
        max_len = 0
        dp  = {}

        for j in range(len(arr)):
            for i in range(j):
                prev = arr[j] -arr[i]
                k = hashmap.get(prev, -1)
                if k >= 0 and k < i:
                    dp[i , j] = dp.get((k , i) , 2) + 1
                    max_len = max(max_len , dp[i , j])
        return max_len if max_len >= 3 else 0
        