
from itertools import combinations
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        fq = defaultdict(list)
        for i, char in enumerate(s):
            fq[char]+=[i]
 
        count = 0
        for indices in fq.values():
            if indices:
                unique_chars = set(s[min(indices)+1:max(indices)])
                count += len(unique_chars)
        return count
