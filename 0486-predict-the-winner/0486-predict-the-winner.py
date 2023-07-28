class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
         
        tb = defaultdict(int)

        def op(nums: List, left: int, right: int):
            if (left, right) not in tb:
                
                if left == right:  return nums[left] 
                tb[(left, right)] = max(nums[left] - op(nums, left + 1, right), nums[right] - op(nums, left, right - 1))
            else:
                return tb[(left, right)]
                
            
            return tb[(left, right)] 
        
        return op(nums, left=0, right=len(nums) - 1) >= 0