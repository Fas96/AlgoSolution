class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start,end=0,len(nums)-1

        while start<=end:
            m=(end+start)//2
            if nums[m]==target:return True
            if nums[start]==nums[m] and nums[m]==nums[end]:
                start+=1
                end+=-1
                continue
            if nums[start]<=nums[m]:
                if nums[start]<=target<nums[m]:
                    end=m-1
                else:
                    start=m+1
            else:
                if nums[m]<target<=nums[end]:
                    start=m+1
                else:
                    end=m-1
        return False
        