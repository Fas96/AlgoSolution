from itertools import permutations
class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lst = list(permutations(digits, 3))
        res = []
        for l in set(lst):
            sVal = int("".join(map(str, l)))
            if sVal % 2 == 0 and l[0]!=0:
                res.append(sVal)
        res.sort()
        return res