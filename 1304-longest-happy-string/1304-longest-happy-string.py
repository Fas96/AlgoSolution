class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count = Counter({'a':a, 'b':b, 'c':c})
        ans = ['$']
        while True:
            (a1, _), (a2, _) = count.most_common(2) 
            if a1 == ans[-1] == ans[-2]:
                a1 = a2 
            if not count[a1]:
                break 
            ans.append(a1)
            count[a1] -= 1   
        return ''.join(ans[1:]) 