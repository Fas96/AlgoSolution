class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        akeys=list(Counter(allowed).keys()) 
        return sum([1 for x in words if  set(list(Counter(x).keys())).issubset(akeys)])
        