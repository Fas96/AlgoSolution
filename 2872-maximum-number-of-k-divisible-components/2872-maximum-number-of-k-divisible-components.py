
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(u, p):
            nonlocal ans
            subtree_sum = values[u]
            for v in adj[u]:
                if v != p:
                    subtree_sum += dfs(v, u)
            if subtree_sum % k == 0:
                ans += 1
                return 0
            return subtree_sum

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = 0
        dfs(0, -1)
        return ans