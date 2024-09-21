class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        a_list=[str(i) for i in range(1,n+1)] 
        return [int(i) for i in sorted(a_list, key = lambda s : s) ]