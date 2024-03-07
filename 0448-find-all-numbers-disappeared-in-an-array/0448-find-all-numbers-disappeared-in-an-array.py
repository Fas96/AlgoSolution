class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        f=Counter(nums)
        ans=[]
        for i in range(1,len(nums)+1):
            if i not in f:
                ans.append(i)
        return ans
        