from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        for ls in set(list(permutations(nums, len(nums)))):
            res.append(list(ls)) 
        
        return res
        