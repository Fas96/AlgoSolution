class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ##base condition 
        if len(nums)<2: return 1
        
        L,R,cnt=0,1,1
        
        while(R<len(nums)):
            if nums[L]==nums[R]:
                R+=1
            elif nums[L]!=nums[R]:
                L+=1
                nums[L],nums[R]=nums[R],nums[L]
                cnt+=1
                R+=1
        return cnt 
 
 