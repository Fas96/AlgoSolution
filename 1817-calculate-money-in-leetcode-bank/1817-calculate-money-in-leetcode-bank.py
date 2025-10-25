class Solution:
    def totalMoney(self, n: int) -> int:
        ans=0
        monday=0
        while n>0:
            if n>7:
                ans += (7 * (1 + monday) + 21)
                n-=7
            else: 
                for i in range(1,n+1): 
                    ans+=(i+monday)
                break
            monday+=1
        return ans
