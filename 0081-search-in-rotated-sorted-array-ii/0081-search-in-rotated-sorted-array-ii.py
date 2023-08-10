class Solution:
    def search(self, nums: List[int], target: int) -> bool:
         
        NN= list(set(nums))
        NN.sort()
        L,R=0,len(NN)-1
    
        while L<=R: 
            M = L+((R-L)//2)
            if NN[M] ==target:
                return True  
            if target > NN[M]:
                L = M + 1
            else:
                 R = M-1
        return False
        