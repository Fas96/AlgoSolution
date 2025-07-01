class Solution:
    def possibleStringCount(self, word: str) -> int:
        freq=Counter(word)
        if len(freq)==1:return len(word)
        mistakes=[word[i]!=word[i-1] for i in range(1, len(word))]
        return len(word)-sum(mistakes)
        