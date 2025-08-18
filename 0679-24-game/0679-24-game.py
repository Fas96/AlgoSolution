class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        n = len(cards)
        if n == 1:
            if abs(24 - cards[0]) < 0.001:
                return True
            return False
        
        for i in range(n):
            for j in range(i + 1, n):
                c1 = cards[i]
                c2 = cards[j]

                arr = [c1 + c2, c1 - c2, c2 - c1, c1 * c2]
                if c1:
                    arr.append(c2 / c1)
                if c2:
                    arr.append(c1 / c2)
                
                for val in arr:
                    nextCards = [val]

                    for k in range(n):
                        if k not in (i, j):
                            nextCards.append(cards[k])
                        
                    if self.judgePoint24(nextCards):
                        return True
        return False
        