class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
         
        ans = 0
         
        mat = defaultdict(lambda: defaultdict(lambda: 2))
         
        for i in range(1, len(nums)):
            for j in range(i):
                df = nums[i]-nums[j]
                if df in mat[j]:
                    mat[i][df] = mat[j][df]+1
                ans = max(ans, mat[i][df])
        return ans
                
            
        