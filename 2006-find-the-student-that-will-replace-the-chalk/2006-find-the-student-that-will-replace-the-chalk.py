class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        idx=0
        n=len(chalk)
        k=k%(sum(chalk))
        while True:
            if idx==n:
                idx=idx%n
            if chalk[idx]>k:
                return idx 
            k-=chalk[idx]
            idx+=1
        return -1 
        