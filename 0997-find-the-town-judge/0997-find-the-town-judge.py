class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        get_trust = [0] * (n + 1)
        give_trust = [0] * (n + 1)

        for a, b in trust:
            give_trust[a] += 1
            get_trust[b] += 1

        for i in range(1, n + 1):
            if give_trust[i] == 0 and get_trust[i] == n - 1:
                return i

        return -1