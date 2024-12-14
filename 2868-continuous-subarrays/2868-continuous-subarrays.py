from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans,n=0,len(nums)
        sw=SortedList()
        idx=0
        for i in range(n):
            sw.add(nums[i])
            while sw[-1]-sw[0]>2:
                sw.remove(nums[idx])
                idx+=1
            ans+=(i-idx+1)
        return ans
        