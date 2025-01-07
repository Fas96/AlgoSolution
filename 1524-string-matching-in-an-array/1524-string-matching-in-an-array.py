class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=set()
        n=len(words)
        for i in range(n):
            for j in range(n):
                if words[i] in words[j] and i != j:
                    print(words[i],words[j])
                    ans.add(words[i]) 
        return list(ans)