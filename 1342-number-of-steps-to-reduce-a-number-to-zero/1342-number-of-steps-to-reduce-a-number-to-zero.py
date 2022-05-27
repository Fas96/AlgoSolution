class Solution:
    count=0
    def numberOfSteps(self, num: int) -> int:
        return sum([1+int(n=='1') for n in bin(num)[2:]]) - 1
        
        