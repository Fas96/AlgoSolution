class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans,n,i=[],len(nums),0 
        while i<n:
            st=nums[i:i+3]
            if st[2] - st[0] > k:
                return []
            ans+=[st]
            i+=3 
        return ans
        