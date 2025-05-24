class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i,w in enumerate(words) if w.count(x)>0]