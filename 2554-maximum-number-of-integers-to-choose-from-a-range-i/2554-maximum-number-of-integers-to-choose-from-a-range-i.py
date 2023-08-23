class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        n=[i for i in range(1,n+1)]
        notInBan = list(set(n)-set(banned))
        notInBan.sort()
        
        res=0
        tt=0
        for x in notInBan:
            if tt+x>maxSum:
                break
            res+=1
            tt+=x
            
        
        return res
        
        