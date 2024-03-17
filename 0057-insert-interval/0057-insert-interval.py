class Solution:
    def insert(self, I: List[List[int]], N: List[int]) -> List[List[int]]:
        ans=[]
        n=len(I)
        start,end=N[0],N[1]
        for i in range(n):
            if I[i][1]<start:ans.append(I[i])
            elif not (end<I[i][0]):
                start=min(start,I[i][0])
                end=max(end,I[i][1])
            else:
                ans.append([start,end])
                return ans+I[i:]
        return ans+[[start,end]]
        