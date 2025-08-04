from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        frq = Counter()
        left = 0
        ans = 0
        
        for right, fruit in enumerate(fruits):
            frq[fruit] += 1 
            while len(frq) > 2:
                lf = fruits[left]
                frq[lf] -= 1
                if frq[lf] == 0:
                    del frq[lf]
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans