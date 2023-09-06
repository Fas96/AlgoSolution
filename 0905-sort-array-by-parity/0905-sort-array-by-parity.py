class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
    
        evn=[]
        odd=[]
        for i,v in enumerate(nums):
            if v&1:
                odd.append(v)
            else:
                evn.append(v)
    
        return evn+odd
        