class Solution:
    def countOdds(self, low: int, high: int) -> int: 
        return  (high+(high&1)-low+(low&1))>>1
        