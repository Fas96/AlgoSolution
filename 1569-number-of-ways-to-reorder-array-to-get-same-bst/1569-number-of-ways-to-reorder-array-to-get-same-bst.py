
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        def combination(nl, nr):
            return factorial[nl+nr]//factorial[nl]//factorial[nr]

        def ways(arrs):
            if len(arrs) <= 2:
                return 1
            root = arrs[0]
            left = [num for num in arrs if num < root]
            right = [num for num in arrs if num > root]
            return ways(left) * ways(right) * combination(len(left), len(right))
        n =len(nums)
        factorial=[1]*(n)
        for idx in range(1,n):
            factorial[idx]=factorial[idx-1]*idx

        return (ways(nums) -1)% mod