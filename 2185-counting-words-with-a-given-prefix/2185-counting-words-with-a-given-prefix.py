class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ctn = 0
        for word in words:
            if word.startswith(pref):
                ctn += 1
        return ctn