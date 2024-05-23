class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = []

        def backtrack(start,curr):
            if len(curr)>0: res.append(curr[:])

            for idx in range(start,len(nums)):
                if nums[idx]+k in curr or nums[idx]-k in curr:
                    continue
                curr.append(nums[idx])
                backtrack(idx+1,curr)
                curr.pop()
        
        backtrack(0,[])
        return len(res)