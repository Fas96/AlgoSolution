class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([1  for x in words  if x.startswith(pref) ])
        