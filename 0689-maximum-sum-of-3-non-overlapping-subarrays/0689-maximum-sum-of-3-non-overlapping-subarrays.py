class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        bestOneIndex = 0
        bestTwoIndex = [0, k]
        bestThreeIndex = [0, k, k*2]

        maxOneTotalSum = sum(nums[:k])
        maxTwoTotalSum = sum(nums[:k*2])
        maxThreeTotalSum = sum(nums[:k*3])

        curOneSum = sum(nums[:k])
        curTwoSum = sum(nums[k:k*2])
        curThreeSum = sum(nums[k*2:k*3])

        n = len (nums)
        for i in range(1, n-k*3+1):
            curOneSum = curOneSum - nums[i-1] + nums [i+k-1]
            curTwoSum = curTwoSum - nums [i+k-1] + nums [i+k*2-1]
            curThreeSum = curThreeSum - nums[i+k*2-1] + nums[i+k*3-1]
            if curOneSum > maxOneTotalSum:
                bestOneIndex = i
                maxOneTotalSum = curOneSum
            if curTwoSum + maxOneTotalSum > maxTwoTotalSum:
                bestTwoIndex = [bestOneIndex, i+k]
                maxTwoTotalSum = curTwoSum + maxOneTotalSum
            if curThreeSum + maxTwoTotalSum > maxThreeTotalSum:
                bestThreeIndex = bestTwoIndex + [i+k*2]
                maxThreeTotalSum = curThreeSum + maxTwoTotalSum
        return bestThreeIndex