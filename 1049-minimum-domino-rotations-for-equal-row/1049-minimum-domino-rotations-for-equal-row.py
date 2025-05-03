class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        for i in [A[0],B[0]]:

            if all(i in d for d in zip(A, B)):

                mod = max(A.count(i), B.count(i))

                return len(A) - mod
        return -1