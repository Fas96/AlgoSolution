class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        self.ans = [[1 for x in range(i)] for i in range(1, numRows + 1)]
        
        
        for i in range(numRows): 
            for j in range(1,i):
                self.ans[i][j]=self.ans[i-1][j-1]+self.ans[i-1][j]
    
        return self.ans