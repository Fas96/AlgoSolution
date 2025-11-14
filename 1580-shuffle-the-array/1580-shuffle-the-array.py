class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        s=nums[n:]
        f=nums[:n+1]
        re=[]
        for i in range(n):
            re+=[f[i],s[i]]
        return re
        