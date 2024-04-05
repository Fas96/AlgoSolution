class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0:return True
        return not (str(num).startswith('0') or  str(num).endswith('0'))
        