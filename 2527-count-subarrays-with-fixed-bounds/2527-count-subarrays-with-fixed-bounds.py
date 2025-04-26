class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans,invalid,mnVal,mxVal = 0,-1,-1,-1
         

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                invalid = i
                continue
            mnVal = i if nums[i] == minK else mnVal
            mxVal = i if nums[i] == maxK else mxVal

            if invalid < mnVal and invalid < mxVal:
                ans += min(mnVal, mxVal) - invalid

        return ans