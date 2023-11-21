class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        rev=[]
        MOD=10**9 + 7
        for n in nums:
            rev.append(n - int(str(n)[::-1])) 
        np = 0
        for n in Counter(rev).values():
            np += n*(n-1)//2 
        return np % MOD
   
                
 