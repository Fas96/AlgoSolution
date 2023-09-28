class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for x in nums:
            if x&1==1:
                odd.append(x)
            else:
                even.append(x)
        return even+odd
        