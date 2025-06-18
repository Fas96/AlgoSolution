class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans,n=[],len(nums)  
        for i in range(0,n,3):
            st=nums[i:i+3]
            if st[2] - st[0] > k:
                return []
            ans+=[st] 
        return ans
        