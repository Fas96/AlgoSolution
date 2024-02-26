import sys
sys.set_int_max_str_digits(0)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s="".join(str(x) for x in num)
        an=str(int(s)+k)
        return [int(x) for x in an]
        