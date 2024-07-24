class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ss=[]
        for n in nums:
            ss.append(int(''.join(str(mapping[int(d)]) for d in str(n))))
           
        return [k for k,_ in sorted(zip(nums,ss),key=lambda a:a[1])]