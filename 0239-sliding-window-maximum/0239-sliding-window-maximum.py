class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if len(nums)<=1: return nums
        # if k==1: return nums

        # ans=[0]*(len(nums)-k+1)
        # print()

        # for i in range(len(ans)):
        #     ans[i]=max(nums[i:i+k])

        # return ans

        heap,answer=[],[]
        for i, num in enumerate(nums):
            heappush(heap,[-num,i])
            while heap and heap[0][1]<=i-k:
                heappop(heap)
            if i>=k-1:
                answer.append(-heap[0][0])
        return answer