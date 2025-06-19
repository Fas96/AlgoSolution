class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        startIndex=0
        numOfSubSeq=float('inf')
        while startIndex<n:
            endOfGroup=nums[startIndex:startIndex+k] 
            startIndex+=1
            if(len(endOfGroup)<k):continue
            numOfSubSeq=min(numOfSubSeq,endOfGroup[-1]-endOfGroup[0])
        return numOfSubSeq
 