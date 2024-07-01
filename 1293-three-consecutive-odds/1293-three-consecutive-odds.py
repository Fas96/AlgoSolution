class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n=len(arr)
        for i in range(n):
            if i+2<n and (arr[i]&1)and (arr[i+1]&1) and (arr[i+2]&1): 
                return True
        return False
        