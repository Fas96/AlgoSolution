class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        i=3
        ans=0
        while True:
            if any(v>1 for v in Counter(nums).values()):
                nums=nums[i:]   
                ans+=1
                
            else:
                break
        return ans

        