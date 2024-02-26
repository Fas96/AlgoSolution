class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N=len(digits)
        s= ''.join(str(x) for x in digits)
        ans=str(int(s)+1)
        return [int(x) for x in ans]