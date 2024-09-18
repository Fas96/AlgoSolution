class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(x) for x in nums]

        def compare(a, b):
            if a+b > b+a:
                return -1
            elif a+b < b+a:
                return 1
            else:
                return 0
            
        nums_str.sort(key=cmp_to_key(compare))

        if nums_str[0] == '0':
            return '0'

        return ''.join(nums_str)