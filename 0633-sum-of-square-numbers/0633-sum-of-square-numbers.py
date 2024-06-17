class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # if c<=2:return True
        
        hashmap={}
        for i,x in enumerate([i*i for i in range(int(sqrt(c))+1)]):
            if x+x==c:return True
            if x in hashmap:
                return True
            hashmap[c-x]=i
        return False
        