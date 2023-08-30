class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        if sorted(nums)==nums:return 0
        
        
        # def is_sorted(l):
        #     return all(a <= b for a, b in zip(l, l[1:]))
        # k=nums
        # cnt=0
        
        
        x = nums[-1]
        res = 0
        for a in reversed(nums):
            k = (a + x - 1) // x
            x = a // k
            res += k - 1
        return res
        
        # while not is_sorted(k):
        #     tm=sorted(k)
        #     if tm[-1]!=tm[-2]:
        #         rem=tm[-1]-tm[-2]
        #         tm=tm[:len(tm)-1]+[rem]+[tm[-2]]
        #     else:
        #         rem=tm[-1]-min(tm)
        #         tm=tm[:len(tm)-1]+[rem]+[min(tm)]
        #     k=tm
        #     cnt+=1 
        # return cnt
    
    
    
        