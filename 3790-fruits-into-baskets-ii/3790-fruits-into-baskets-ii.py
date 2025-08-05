class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        N=len(fruits)
        placed=[False]*N 
        for j in range(N):
            for b in range(N):
                if fruits[j]<=baskets[b] and not placed[b]: 
                    placed[b]=True
                    break
         
        return  sum(not p for p in placed)
        