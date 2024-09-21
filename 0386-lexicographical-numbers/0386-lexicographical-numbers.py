class Solution:
    def lexicalOrder(self, n: int) -> List[int]: 
        return [int(i) for i in sorted([str(i) for i in range(1,n+1)] , key = lambda s : s) ]