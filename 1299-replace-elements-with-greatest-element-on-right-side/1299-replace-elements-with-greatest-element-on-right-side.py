class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N=len(arr)
        ans=[-1]*N  
        mx=-1
        for i in range(N-1,-1,-1):
            mx=max(mx, ans[i])
            ans[i], mx = mx, max(mx, arr[i])
        ans[-1]=-1
        return ans
            
            
        