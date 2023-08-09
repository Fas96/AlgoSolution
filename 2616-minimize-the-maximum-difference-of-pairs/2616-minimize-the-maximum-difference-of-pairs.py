class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l, r = 0, max(nums)
        N= len(nums)
        
        def letCheckPairsCount(mid):
            cnt=0
            idx=0
            while idx< N-1:
                if nums[idx+1]-nums[idx]<=mid:
                    cnt+=1
                    idx+=2
                else:
                    idx+=1 
            return cnt >= p
        
        while l < r:
            mid = l+((r - l) >> 1)
            if letCheckPairsCount(mid):
                r = mid
            else:
                l = mid + 1
        return l
        
    