class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        XX= [k for k, v in Counter(nums).items() if v == 2]
        return reduce(xor,XX) if len(XX)>0 else 0