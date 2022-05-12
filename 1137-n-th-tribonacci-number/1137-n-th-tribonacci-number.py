class Solution:
    def tribonacci(self, n: int) -> int:
        T0,T1,T2=0,1,1
        if n==1 or n==2: return T2
        
        T_N=0
        
        for i in range(3,n+1):
            T_N=T0+T1+T2
            T0=T1
            T1=T2
            T2=T_N
        return T_N
    
        
        
        