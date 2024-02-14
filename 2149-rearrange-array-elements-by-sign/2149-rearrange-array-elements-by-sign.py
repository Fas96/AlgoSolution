class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        li,li1,res=[],[],[]
        for i in nums:
            if i>0:   li.append(i)
            else:   li1.append(i)
        for i in range(len(li)):
            res.extend([li[i],li1[i]])
        return res