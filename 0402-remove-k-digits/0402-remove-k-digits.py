import sys
sys.set_int_max_str_digits(0)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        for x in num:
            while stk and k > 0 and stk[-1] > x:
                stk.pop()
                k -= 1
            stk.append(x)

        while stk and k > 0:
            stk.pop()
            k -= 1
        return "0" if not stk else str(int("".join(stk)))
        