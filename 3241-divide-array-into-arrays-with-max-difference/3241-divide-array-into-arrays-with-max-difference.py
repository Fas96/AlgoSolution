class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        i=0
        while i<n:
            if nums[i:i+3][2] - nums[i:i+3][0] > k:
                return []
            ans.append(nums[i:i+3])
            i+=3 
        return ans
        