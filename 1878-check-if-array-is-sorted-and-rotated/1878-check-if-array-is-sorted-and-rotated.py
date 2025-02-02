class Solution:
    def check(self, B: List[int]) -> bool:
        A=sorted(B)
        n=len(A)
        for i in range(n):
            if A[i:]+A[:i]==B:
                return True
        return False