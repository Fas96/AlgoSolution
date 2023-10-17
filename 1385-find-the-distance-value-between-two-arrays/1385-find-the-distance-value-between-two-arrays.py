class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
 
        def bs(ns,t):
            ns.sort()
            l,r=0,len(ns)-1
            while l<=r:
                m=(l+r)//2
                if ns[m]==t:
                    return m
                if ns[m]<t:
                    l=m+1
                else:
                    r=m-1
            return -1
        ans=0
        for x in arr1:
            xx=bs(arr2,x)
            if xx==-1 and all([abs(x-k)>d for k in arr2]):
                ans+=1
         
        return ans
            
        