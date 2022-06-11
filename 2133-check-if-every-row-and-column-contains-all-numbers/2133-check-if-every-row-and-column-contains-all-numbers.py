class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)):
            if len(matrix[i]) != len(set(matrix[i])):
                return False

        for i in range(len(matrix)):
            st = set()
            lt = []
            for j in range(len(matrix)):
                st.add(matrix[j][i])
                lt.append(matrix[j][i])
            if len(st) != len(lt):
                return False
        return True