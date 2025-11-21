
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        fq = defaultdict(list)
        for i, char in enumerate(s):
            fq[char]+=[i] 
        return sum([len(set(s[min(indices)+1:max(indices)])) for indices in fq.values() if indices])
