class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[0])

        def dfs(events, k, idx, memo):
            if k == 1:
                mx = 0
                while idx < len(events):
                    mx = max(events[idx][2], mx)
                    idx += 1
                return mx
            if memo[k][idx] != -1:
                return memo[k][idx]
            res = 0
            for i in range(idx, len(events)):
                cur = events[i][2]
                for j in range(i + 1, len(events)):
                    if events[j][0] > events[i][1]:
                        res = max(res, cur + dfs(events, k - 1, j,memo))
                res = max(res, cur)
            memo[k][idx]=res
            return  memo[k][idx]

        memo = [[-1] * len(events) for _ in range(k + 1)]

        return dfs(events, k, 0, memo)
        