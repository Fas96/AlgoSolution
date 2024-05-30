class Solution:
    def countTriplets(self, arr: List[int]) -> int: 
        n=len(arr)
        ans=0
        for i in range(n):
            value=arr[i]
            for j in range(i+1,n):
                value=value^arr[j]
                if value==0:
                    ans+=(j-i)
                    
        return ans
        