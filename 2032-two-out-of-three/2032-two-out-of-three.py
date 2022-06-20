class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        join = list(set(nums1 + nums2 + nums3))
        res=[]
        for v in join:
            cnt = 0
            if v in nums1:
                cnt += 1
            if v in nums2:
                cnt += 1
            if v in nums3:
                cnt += 1
            if cnt>=2:
                res.append(v)
 
        return res