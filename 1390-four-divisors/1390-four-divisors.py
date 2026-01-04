class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def factors(n):
            if n < 1:
                return []
            
            ans = []
             
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    ans.append(i) 
                    if i != n // i:
                        ans.append(n // i) 
            ans.sort()
            return ans
        re=0
        for n in nums:
            v=factors(n)
            if len(v)==4:
                re+=sum(v)
        return re
        