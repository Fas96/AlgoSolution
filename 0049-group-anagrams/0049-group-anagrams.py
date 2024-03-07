class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq=defaultdict(list)
        for x in strs: 
            freq["".join(sorted(x))].append(x)
        return freq.values()
        