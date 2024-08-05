class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp=Counter(nums)   
        return [ky for ky,v in sorted(mp.items(),key=lambda item:-item[1])][:k]

        