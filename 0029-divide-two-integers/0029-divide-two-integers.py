from decimal import Decimal
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return min(int(str(dividend/divisor).split('.')[0]),2**31-1) 
        