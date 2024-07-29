class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        res = 0
        for i in range(1, n - 1):
            less = [0, 0]
            greater = [0, 0]
            for j in range(n):
                if rating[i] < rating[j]:
                    less[1 if j > i else 0] += 1
                if rating[i] > rating[j]:
                    greater[1 if j > i else 0] += 1
            res += less[0] * greater[1] + greater[0] * less[1]
        return res