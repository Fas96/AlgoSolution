class Solution:
    def lexicalOrder(self, n: int) -> List[int]: 
        al = []
        curr = 1
        for i in range(1, n + 1):
            al.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr >= n:
                    curr //= 10
                curr += 1
        return al
        # return [int(i) for i in sorted([str(i) for i in range(1,n+1)] , key = lambda s : s) ]