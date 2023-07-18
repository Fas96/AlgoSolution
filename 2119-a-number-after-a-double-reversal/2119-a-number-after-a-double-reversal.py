class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if len(str(num))==1 or len(set(str(num)))==1:
            return True
        n =len(str(num))
        
        return False if str(num)[-1] == "0" else True
        
        