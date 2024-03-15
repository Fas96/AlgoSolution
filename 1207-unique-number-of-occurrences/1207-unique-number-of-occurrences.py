class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f=list(Counter(arr).values())
        return len(set(f))==len(f)
        