class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        f=Counter(nums)
        ans=[]
        for i in range(1,len(nums)+1):
            if not f[i]:
                ans.append(i)
        return ans
        