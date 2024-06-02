class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        inter=arrays[0]
        
        for n in range(1,len(arrays)):
            inter=set(inter).intersection(set(arrays[n]))
        
        ans=sorted(list(inter))
         
        return ans