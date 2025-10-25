class Solution:
    def totalMoney(self, n: int) -> int:
        ans=0
        add=0
        while n>0:
            if n>7:
                ans += (7 * (1 + add) + 21)
                n-=7
            else: 
                for i in range(1,n+1):
                    print(i+add)
                    ans+=(i+add)
                break
            add+=1
        return ans
