class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        def dfs(nums,idx,diff,ans):
            if (idx,diff) in ans:
                return ans[(idx,diff)]
            
            if idx >=len(nums):
                if diff:
                    return float('-inf')
                return 0
            
            long=dfs(nums,idx+1,diff+nums[idx],ans)
            skip=dfs(nums,idx+1,diff,ans)
            short=dfs(nums,idx+1,abs(nums[idx]-diff),ans)+min(diff,nums[idx])
            
            ans[(idx,diff)]=max(long,short,skip)
            return ans[(idx,diff)]   
        
        
        ans={}
        return dfs(rods,0,0,ans)
        