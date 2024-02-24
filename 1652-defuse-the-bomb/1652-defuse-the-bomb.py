class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N=len(code)
        if k==0:
            return [0]*N
        
        
        ans=[0]*N
        if k > 0:
          
            for i in range(N):
                sm = 0
                for j in range(1, k + 1): 
                    sm += code[(i + j) % N] 
                ans[i] = sm
        else:
            for i in range(N):
                sm = 0
                for j in range(1, -k + 1): 
                    sm += code[(i - j) % N] 
                ans[i] = sm
        return ans
            
            
        