class Solution:
    def countOrders(self, n: int) -> int:
        mod=10**9+7
        ans=math.factorial(n*2)>>n
        return ans%mod
        