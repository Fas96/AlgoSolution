class Solution:
    def judgeSquareSum(self, c: int) -> bool: 
        hashmap={}
        for i,x in enumerate([i*i for i in range(int(sqrt(c))+1)]):
            
            if( x in hashmap) or  (x+x==c): return True
            hashmap[c-x]=i
        return False
        