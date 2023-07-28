class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
         
        tb = defaultdict(int)

        def op(nums: List, left: int, right: int):
            if (left, right) not in tb:
                # last one remaining
                if left == right:
                    return nums[left]
               
                p_left = nums[left] - op(nums, left + 1, right)
                p_right = nums[right] - op(nums, left, right - 1)

                tb[(left, right)] = max(p_left, p_right)
            else:
                return tb[(left, right)]
                
            
            return tb[(left, right)] 
        
        return op(nums, left=0, right=len(nums) - 1) >= 0