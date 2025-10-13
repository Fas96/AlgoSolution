class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]: 
        n, l=len(words), 0
        ans=[words[0]]
        startFreq=Counter(words[0])
        for r in range(1, n):
            s=words[r]
            x=Counter(s)
            if startFreq!=x:
                ans.append(s)
                l=r
                startFreq=x
        return ans 

        