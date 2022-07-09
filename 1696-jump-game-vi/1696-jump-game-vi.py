class Solution(object):
    def maxResult(self, nums, k):
        dq = deque()
        for i in range(len(nums)):
          nums[i] += nums[dq[0]] if len(dq) else 0
          while dq and i - dq[0] >= k:
            dq.popleft()
          while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
          dq.append(i)
        return nums[-1]