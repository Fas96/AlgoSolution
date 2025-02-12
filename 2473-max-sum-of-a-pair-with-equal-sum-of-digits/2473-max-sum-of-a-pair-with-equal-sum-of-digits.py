class Solution: 
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(num):
            return sum(map(int, str(num)))
        nums.sort()
        sum_to_num = {}
        max_sum = -1

        for num in nums:
            curr_sum = digit_sum(num)

            if curr_sum in sum_to_num:
                max_sum = max(max_sum, sum_to_num[curr_sum] + num)

            sum_to_num[curr_sum] = num
        
        return max_sum