class Solution:
    def getRow(self, rowIndex: int) -> List[int]: 
        
        if rowIndex == 0:
            # Base case
            return [1]
        
        elif rowIndex == 1:
            # Base case
            return [1, 1]
        
        else:
            # General case:
            last_row = self.getRow( rowIndex-1 )
            size = len(last_row)
            return [ last_row[0] ] + [ last_row[idx] + last_row[idx+1] for idx in range( size-1) ] + [ last_row[-1] ]