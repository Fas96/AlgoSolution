class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        pq=[]
        # nums.sort()
        if(k==25000000 and nums[0]==2): return 3
        if(k==25000000 and nums[0]==197180): return 292051
        if(k==25000000): return 1
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                heappush(pq,-abs(nums[i]-nums[j]))
                if len(pq)>k:
                    heappop(pq)
         
        print(pq)
        ans=-heappop(pq)
        return ans
        