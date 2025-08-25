class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
  
        r, c = len(mat), len(mat[0])
        result = [] 
        for diagonal in range(r + c - 1):
            temp = [] 
            for i in range(r):
                j = diagonal - i
                if 0 <= j < c: 
                    temp.append(mat[i][j])
            
            if diagonal % 2 == 0:
                temp.reverse()
            
            result.extend(temp)
        
        return result
        # [0,0]

        # [0,1],[1,0]

        # [0,2],[1,1],[0,2]

        # [1,2],[2,2],

        # [2,3]

        return []