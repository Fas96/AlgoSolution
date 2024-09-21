class Solution:
    def lexicalOrder(self, n: int) -> List[int]: 
        ans = []
        start = 1
        for i in range(1, n + 1):
            ans.append(start)
            if start * 10 <= n:
                start *= 10
            else:
                while start % 10 == 9 or start >= n:
                    start //= 10
                start += 1
        return ans
        # return [int(i) for i in sorted([str(i) for i in range(1,n+1)] , key = lambda s : s) ]