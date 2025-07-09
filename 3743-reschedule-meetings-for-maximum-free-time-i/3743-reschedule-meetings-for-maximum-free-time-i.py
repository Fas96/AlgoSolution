class Solution:
    def maxFreeTime(self, event: int, k: int, start: List[int], end: List[int]) -> int:
        time=0
        free=[]
        for i in range(len(start)):
            free.append(start[i]-time)
            time=end[i]
        free.append(event-time)
        # print(free)
        k+=1
        sums=sum(free[:k])
        ans=sums
        for i in range(k,len(free)):
            sums-=free[i-k]
            sums+=free[i]
            ans=max(ans,sums)
        return ans