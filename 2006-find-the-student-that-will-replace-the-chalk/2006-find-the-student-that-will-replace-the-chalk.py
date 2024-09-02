class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        ac=list(accumulate(chalk)) 
        return bisect_right(ac, k%ac[-1])
        