class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        sbit=['0']*len(s)
        N=len(s)
        leftMost=0 
        
        for i,c in enumerate(s):
            if c=='1':
                if '1' not in sbit: sbit[N-1]='1'
                else: 
                    sbit[leftMost]='1'
                    leftMost+=1 
        
        print(sbit)
        
        
        return "".join(sbit)
        