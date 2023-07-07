class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        N, left, ans, dd = len(answerKey), 0, 0, defaultdict(int)

        for i in range(N):
            dd[answerKey[i]] += 1
            while dd['T'] > k and dd['F'] > k:
                dd[answerKey[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans
        