class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        def DFS(n, left, right):
            left, right = min(left, right), max(left, right)
            if left + right == n + 1:
                return (1, 1)
            if n == 3 or n == 4:
                return (2, 2)
            if left - 1 > n - right:
                left, right = n + 1 - right, n + 1 - left
            nextRound = (n + 1) // 2
            minRound, maxRound = n , 1
            if right * 2 <= n + 1:
                preL = left - 1
                gap = right - left - 1
                for i in range(preL + 1):
                    for j in range(gap + 1):
                        res = DFS(nextRound, i + 1, i + j + 2)
                        minRound = min(minRound, 1 + res[0])
                        maxRound = max(maxRound, 1 + res[1])
            else:
                preR = n + 1 - right
                preL = left - 1
                mid = preR - left - 1
                innerGap = right - preR - 1
                for i in range(preL+ 1):
                    for j in range(mid + 1):
                        position1 = i + 1
                        position2 = i + j + 1 + (innerGap + 1) // 2 + 1
                        res = DFS(nextRound, position1, position2)
                        minRound = min(minRound, 1 + res[0])
                        maxRound = max(maxRound, 1 + res[1])
            return (minRound, maxRound)
        return list(DFS(n, firstPlayer, secondPlayer))