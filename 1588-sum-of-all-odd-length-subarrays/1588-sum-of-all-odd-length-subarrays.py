class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        ans=0
        for i in range(n):
            for j in range(i,n):
                a=arr[i:j+1]
                if len(a)%2==1:
                    ans+=sum(a)
        return ans
                    
        