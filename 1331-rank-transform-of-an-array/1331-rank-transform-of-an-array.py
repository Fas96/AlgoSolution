class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        def bsleft(nums: List[int], target: int):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + ((r - l) >> 1)
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        nums = sorted(list(set(arr)))
        res = []
        for i in arr:
            res.append(bsleft(nums, i) + 1)
        return res