class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        L,R,N=0,k,len(nums)
          
        ff=sum(nums[0:k])/k
        tem=ff
        while R<N:
            ff=(ff-(nums[L])/k)
            ff=(ff+(nums[R])/k)
            L+=1
            R+=1
            tem=max(ff,tem)
         
        return tem