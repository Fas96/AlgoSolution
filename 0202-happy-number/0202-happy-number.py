class Solution:
    def isHappy(self, n: int) -> bool:
        def numSqSum(n):
            sq = 0
            while n:
                sq += (n % 10) * (n % 10)
                n = int(n / 10)
            return sq
        sl=fs=n
        while True:
            sl=numSqSum(sl)
            fs=numSqSum(numSqSum(fs))
            if sl!=fs:continue
            else: break
        return sl==1
        