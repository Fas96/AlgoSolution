class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        L,R=0,0
        while R<len(nums):
            if nums[R]!=val:
                nums[L]=nums[R]
                L+=1
            R+=1
        print(nums)
        return L
                
        
        
     
        