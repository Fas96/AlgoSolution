class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans=[]
        n=len(nums)
        right=0
        for i, num in enumerate(nums):
            if num==key:
                left=max(right,i-k)
                right=min(n,i+k+1)
                ans.extend(range(left,right))
        return ans


        