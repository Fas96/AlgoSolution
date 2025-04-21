class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        num = 0
        biggest = 0
        smallest = 0

        for i in differences:
            num += i
            if num > biggest:
                biggest = num
            elif num < smallest:
                smallest = num
            if upper - lower < biggest - smallest:
                return 0
        
        return (upper - lower) - (biggest - smallest) + 1