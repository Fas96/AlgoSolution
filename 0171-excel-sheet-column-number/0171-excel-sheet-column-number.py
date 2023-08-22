class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        result = 0
        for x in columnTitle:
            result=(result * 26)+ (ord(x)-65+1)
        return result
 
    
    
        