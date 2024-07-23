class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        an=[]
        for k,v in sorted(Counter(nums).items(), key=lambda t: (t[1], -t[0])):
            an+=([k]*v)
        return an
        