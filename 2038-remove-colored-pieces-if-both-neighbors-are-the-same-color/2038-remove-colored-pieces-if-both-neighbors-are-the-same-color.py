class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        AP, BP = 0, 0
        count = 1 
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                count += 1
            else:
                if colors[i - 1] == 'A':
                    AP += max(0, count - 2)
                else:
                    BP += max(0, count - 2)
                count = 1
        
        if colors[-1] == 'A':
            AP += max(0, count - 2)
        else:
            BP += max(0, count - 2)
        
        return AP > BP
        