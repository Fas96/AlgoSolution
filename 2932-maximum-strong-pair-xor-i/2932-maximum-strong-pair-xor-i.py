class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        L,R,N=0,0,len(nums)
        ans=[]
        aa=[]
        
        while R<N:
            K=R
            while K<N:
                if abs(nums[L] - nums[K])<= min(nums[L],nums[K]):
                    ans.append(max((nums[L] ^ nums[K]), (nums[K]^nums[L])) )
                aa.append([nums[L] , nums[K]])
                K+=1
            R+=1
            L=R
        print(aa)
        return max(ans)
            
                
        