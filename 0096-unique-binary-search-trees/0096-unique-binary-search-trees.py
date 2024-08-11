
'''
The number of unique binary search trees that can be formed with n vertices is called the nth Catalan number.

nth Catalan number is given by 2nCn/(n+1).
'''
class Solution:
    def numTrees(self, n: int) -> int:
        return math.comb(2*n,n)//(n+1)
        

        '''
        nth Catalan number is given by 2nCn/(n+1).
        '''