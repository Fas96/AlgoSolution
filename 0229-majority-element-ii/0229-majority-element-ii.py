class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp=Counter(nums)
        ans=[]
        N=len(nums)
        for x in set(nums):
            if mp.get(x)>floor(N/3):
                ans.append(x)
            
        return ans
        