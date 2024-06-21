class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_sat = 0
        powerup = 0

        for i in range(len(customers)):
            max_sat += customers[i] * (1 - grumpy[i])
            customers[i] *= grumpy[i]

            if i > 0:
                customers[i] += customers[i - 1]
            
            if i == minutes - 1:
                powerup = customers[i]
            
            if i >= minutes:
                curr = customers[i] - customers[i - minutes]
                powerup = max(powerup, curr)
        
        return max_sat + powerup
        
        
        
        