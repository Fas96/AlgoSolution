class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp=Counter(nums) 
        N=len(nums)
       
        return [x for x in set(nums) if mp.get(x)>floor(N/3)]
        