class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #return list(set([x for x in nums1 if (x in nums1 and x in nums2)]))
        nums1.sort()
        nums2.sort()
        def bs(nums,t):
            l,r=0,len(nums)-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==t:
                    return nums[m]
                elif nums[m]<t:
                    l=m+1
                else:
                    r=m-1 
            return None
        ans=[]
        for x in nums1:
            if bs(nums2,x) is not None  and (x not in ans):
                ans.append(x)
        return ans
                    
    
        