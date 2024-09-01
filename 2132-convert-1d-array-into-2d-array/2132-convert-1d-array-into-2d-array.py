class Solution:
    def construct2DArray(self, og: List[int], m: int, n: int) -> List[List[int]]:
        if  len(og)%m!=0:return []
        ans=[]
        temp=[]
        for x in og:
            temp.append(x)
            if len(temp)==n:
                ans.append(temp)
                temp=[]
        if m*n!=len(og):return []
        
        if len(ans)>0 and len(ans[0])<n:return []
        
        if len(ans)>m: return []

        return ans

            
        