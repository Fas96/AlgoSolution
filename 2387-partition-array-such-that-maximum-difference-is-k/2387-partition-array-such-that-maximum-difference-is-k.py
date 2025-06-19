class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        numOfSubSeq=startIndex=0
        while startIndex<n:
            endOfGroup=nums[startIndex]+k
            startIndex=bisect_right(nums,endOfGroup,startIndex)
            numOfSubSeq+=1
        return numOfSubSeq