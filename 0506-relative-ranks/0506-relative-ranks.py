class Solution:
    def findRelativeRanks(self, S: List[int]) -> List[str]:
        hq = []
        for i, s in enumerate(S):
            heapq.heappush(hq, (-s, i))

        ranks = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}

        ans = [0] * len(S)

        for rank in range(len(S)):
            _, idx = heapq.heappop(hq)
            ans[idx] = ranks.get(rank, str(rank + 1))

        return ans 