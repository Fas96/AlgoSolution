class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N=len(arr)
        ans=[-1]*N  
        mx=-1
        for i in range(N-1,-1,-1):
            ans[i], mx = mx, max(mx, arr[i])
        return ans
            
            
        