class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N1=len(nums1)
        ans=[-1]*(N1)
        for idx,x in enumerate(nums1):
            xx=nums2.index(x)
            cnt=0 
            for y in nums2[xx:]:
                if y>x:
                    cnt=y
                    break
            ans[idx]=cnt if cnt!=0 else -1
        return ans