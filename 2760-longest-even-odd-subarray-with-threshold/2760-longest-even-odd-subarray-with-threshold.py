class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        L,res,n=0,0,len(nums) 
        R=L
        while R<n:
            while R < n and nums[L]%2==0 and nums[R]<=threshold:
                if R<n-1 and (nums[R+1]%2==nums[R]%2 or nums[R+1]>threshold): 
                    break
                R+=1
            if nums[L]%2==0 : 
                if R==n: 
                    R-= 1
                if nums[R]<=threshold: 
                    res = max(res , R-L+1)
            R+=1;L=R
        return res