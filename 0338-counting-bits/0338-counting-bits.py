class Solution:
    def countBits(self, n: int) -> List[int]: 
        def bit_count(a):
            cnt=0
            while a:
                cnt+= (a&1)
                a >>=1
            return cnt
        bf=[0]
        for i in range(1,n+1):
            bf.append(bit_count(i))
        return bf
        
        # dp = [0] * (n + 1)
        # offset = 1
        # for i in range(1, n + 1):
        #     if offset * 2 == i:
        #         offset = i
        #     dp[i] = 1 + dp[i - offset]
        # return dp