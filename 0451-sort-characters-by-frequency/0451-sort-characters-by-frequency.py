class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([c * occ for c, occ in sorted(Counter(s).items(), key = lambda pair : pair[1], reverse = True)])  