class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def digitsA(n):
            ar = []
            while n > 0:
                digit = n % 10
                ar.append(str(mapping[digit]))
                n = n // 10
            
            return int(''.join(ar)[::-1],base=10)
        ss=[]
        for n in nums:
            if n==0:
                ss.append(mapping[n])
            else: ss.append(digitsA(n))
           
        return [k for k,v in sorted(zip(nums,ss),key=lambda a:a[1])]