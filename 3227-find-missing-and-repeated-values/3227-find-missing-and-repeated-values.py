class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = {}

        
        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1
 
        a = []
         
        for i in range(1, n*n + 1):
            if i not in freq:
                m=i 
            elif freq[i]==2:
                r=i 
       
        return [r,m]