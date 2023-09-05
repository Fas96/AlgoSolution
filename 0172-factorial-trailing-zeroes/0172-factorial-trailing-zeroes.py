sys.set_int_max_str_digits(0)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        
        def go(n):
            if n ==1:
                return 1
            if n ==0:
                return 0
            return n*go(n-1)
        
        result = go(n)
        if result==0:
            return 0
        print(result,str(result)[::-1])
        cnt=0
        for x in list(str(result)[::-1]): 
            if int(x)>0:
                break
            cnt+=1
            
        return cnt
        