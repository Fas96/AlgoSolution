class Solution(object):
    def checkPossibility(self, nums):
        l = nums[:]
        k = nums[:]

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                l[i] = nums[i + 1]
                k[i + 1] = nums[i]
                break
        return l == sorted(l) or k == sorted(k)