class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        invalid = -1
        mnVal = -1
        mxVal = -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                invalid = i
                continue
            mnVal = i if nums[i] == minK else mnVal
            mxVal = i if nums[i] == maxK else mxVal

            if invalid < mnVal and invalid < mxVal:
                answer += min(mnVal, mxVal) - invalid

        return answer