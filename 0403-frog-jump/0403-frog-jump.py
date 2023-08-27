class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]!=1:  return False
        n=len(stones)
        cache=[[False] * n for _ in range(n)]
        
         
        def recurJump(ss,lastIdx,curIdx):
            if curIdx==len(ss)-1:
                return True
            if cache[lastIdx][curIdx]: return False
            
            lastJump=ss[curIdx]-ss[lastIdx]
            nextIdx=curIdx+1
            
            while nextIdx<len(ss) and ss[nextIdx]<=ss[curIdx]+lastJump+1:
                nextJump=ss[nextIdx]-ss[curIdx]
                jump=nextJump-lastJump
                
                
                if jump>=-1 and jump<=1:
                    if recurJump(ss,curIdx,nextIdx):
                        return True
                nextIdx+=1
                
            cache[lastIdx][curIdx]=True
            
            return False
        
        return recurJump(stones,0,1)
         
        
        