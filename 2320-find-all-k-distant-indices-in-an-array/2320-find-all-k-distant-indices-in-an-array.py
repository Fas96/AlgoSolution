class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans=set()
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if abs(i-j)<=k and nums[j]==key:
                    ans.add(i)
        return sorted(list(ans))


        