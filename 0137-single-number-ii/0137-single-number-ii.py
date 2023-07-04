class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        
        d = defaultdict(dict)
        for num in nums: d[num] = d.get(num, 0) + 1
        for k, v in d.items():
            if v == 1:
                return k
        return -1
        