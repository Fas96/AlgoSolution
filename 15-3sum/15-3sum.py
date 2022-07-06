class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        
        if len(nums)<3:
            return []
        
        for i in range(len(nums)-1):
            if i!=0 and nums[i]==nums[i-1]: continue
            L,R=i+1,len(nums)-1
            while L<R:
                curSum=nums[L]+nums[R]+nums[i] 
                if curSum==0:
                    res.append([nums[L],nums[R],nums[i]])
                    L+=1
                    R-=1
                    while L<R and nums[L]==nums[L-1]:
                        L+=1
                    while L<R and nums[R]==[R+1]:
                        R-=1
                elif curSum<0:
                    L+=1
                else:
                    R-=1
        return res
                
            
        