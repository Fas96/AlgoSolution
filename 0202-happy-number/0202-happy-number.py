class Solution:
    def isHappy(self, n: int) -> bool:
        def numSquareSum(n):
            squareSum = 0
            while(n):
                squareSum += (n % 10) * (n % 10)
                n = int(n / 10)
            return squareSum
        sl=fs=n
        while True:
            sl=numSquareSum(sl)
            fs=numSquareSum(numSquareSum(fs))
            if sl!=fs:continue
            else: break
        return sl==1
        