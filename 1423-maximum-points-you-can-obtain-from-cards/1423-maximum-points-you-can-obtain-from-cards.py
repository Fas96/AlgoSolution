class Solution(object):
    def maxScore(self, cardPoints, k):
        N = len(cardPoints)
        i = 0
        j = N - k
    
        total = sum(cardPoints[j:])
        best = total
        for _ in range(k):  
            total += cardPoints[i] - cardPoints[j]
            best = max(best, total)
            i += 1
            j += 1
        return best

        