class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        pow=[str(2**i) for i in range(31)] 

        N,freqN=len(str(n)),Counter(str(n)) 
         
        eqN=[pp for pp in pow if len(pp)==N]
       
        return any(Counter(c)==freqN  for c in eqN)
        
        