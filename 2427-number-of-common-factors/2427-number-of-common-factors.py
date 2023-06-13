class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        def numFactors(num:int):
            factors = set()
            for i in range(1,int(math.sqrt(num))+1):
                if num%i == 0:
                    factors.add(i)
                    factors.add(num//i)
            return factors 
        return  (len(numFactors(a).intersection(numFactors(b)))) 