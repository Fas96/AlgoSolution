class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        i = 1
        
        while i < len(flowerbed) - 1:
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                n -= 1
                i += 1
                
            if n <= 0:
                return True
            
            i += 1