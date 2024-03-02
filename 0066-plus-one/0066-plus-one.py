class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N=len(digits)
        pos=10
        NUM=0
        for x in digits:
            NUM = (NUM*pos)+ (x) 
        NUM+=1
        return [int(d) for d in str(NUM)]
        