class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n=len(words)
        ans=0
        def isPrefixAndSuffix(a,b):
            return b.startswith(a) and b.endswith(a)
        for i in range(n):
            for j in range(i+1,n):
                if isPrefixAndSuffix(words[i],words[j]):
                    ans+=1
        return ans
        