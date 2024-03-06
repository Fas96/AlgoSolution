class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ff = [0] + flowerbed + [0] 
        for i in range(1,len(ff)-1):
            if ff[i-1] == ff[i] == ff[i+1] == 0:
                n -= 1 
                ff[i] = 1
            if n <= 0:
                return True
        return n<=0