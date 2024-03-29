class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        L,R,N=0,0,len(nums)
        ans=[]
        
        while R<N:
            K=R
            while K<N:
                if abs(nums[L] - nums[K])<= min(nums[L],nums[K]):
                    ans.append(max((nums[L] ^ nums[K]), (nums[K]^nums[L])) )
                K+=1
            R+=1
            L=R 
        return max(ans)
            
                
        