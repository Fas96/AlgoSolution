class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        for i in range(n//2+1):
            ans.append(i)
        for i in range(1,n//2+1):
            ans.append(-i) 
        if len(ans)>n:
            ans=ans[1:]
        return ans
        