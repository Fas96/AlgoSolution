class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        M,N=len(queries),len(nums)
        nums.sort()
        ans=[]
        def BS(row,t):
            l,r=0,len(row)-1
            while l<=r:
                m=(l+r)//2
                if row[m]<=t:
                    l=m+1
                else:
                    r=m-1 
            return l
        pf=list(accumulate(nums))
        print(pf) 
        for x in queries:
            xx=BS(pf,x)
            ans.append(xx)
        return ans
            
            