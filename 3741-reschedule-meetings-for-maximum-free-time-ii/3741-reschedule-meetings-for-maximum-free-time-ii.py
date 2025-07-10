class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        vmax=0
        n=len(startTime)
        
        st=startTime+[eventTime]
        et=[0]+endTime
        
        big3={(0,-1),(0,-2),(0,-3)}#(space,index)
        
        no3=(0,-1)
        for i in range(n+1):
            sp=st[i]-et[i]
            
            if sp>no3[0]:
                big3.discard(no3)
                big3.add((sp,i))
                no3=min(big3)
                
        no1=max(big3)
        big3.discard(no1)
        big3.discard(no3)
        no2=list(big3)[0]
        

        for i in range(n):
            l=et[i+1]-st[i]
            if i<no1[1]-1 or i>no1[1]:
                maxroom=no1[0]
            elif i==no1[1]-1==no2[1] or i==no1[1]==no2[1]-1:
                maxroom=no3[0]
            else:
                maxroom=no2[0]

            if maxroom>=l:
                mft=st[i+1]-et[i]
            else:
                mft=st[i+1]-et[i]-l
            vmax=max(vmax,mft)
        return vmax