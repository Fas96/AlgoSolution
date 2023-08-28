import math
import operator as op
from functools import reduce


class Solution:
    def numTrees(self, n: int) -> int:
        def catalan_recursive(n):
            return 1 if n == 0 else (2 * (2 * n - 1) * catalan_recursive(n - 1)) // (n + 1)
        return catalan_recursive(n)
        