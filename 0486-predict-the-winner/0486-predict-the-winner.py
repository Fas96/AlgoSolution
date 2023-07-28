class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
         
        self.tb = defaultdict(int)

        def op(nums: List, left: int, right: int):

            if left == right:
                return nums[left]

            if (left, right) in self.tb:
                return self.tb[(left, right)]
            choose_left = nums[left] - op(nums, left + 1, right)
            choose_right = nums[right] - op(nums, left, right - 1)

            self.tb[(left, right)] = max(choose_left, choose_right)
            return self.tb[(left, right)] 
        
        return op(nums, left=0, right=len(nums) - 1) >= 0