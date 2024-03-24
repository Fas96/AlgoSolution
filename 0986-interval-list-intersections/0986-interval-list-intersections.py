class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        i, j, start, end = 0, 0, 0, 1
        

        while i < len(A) and j < len(B):
            A_O_B = A[i][0] >= B[j][0] and A[i][0] <= B[j][1]
            B_O_A = B[j][0] >= A[i][0] and B[j][0] <= A[i][1]
            if (A_O_B or B_O_A):
                result.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return result
        