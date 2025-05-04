class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_counts = defaultdict(int)
        for domino in dominoes:
            normalized = tuple(sorted(domino))
            domino_counts[normalized] += 1
        print(domino_counts)
        
        ans = 0
        for count in domino_counts.values():
            if count >= 2:
                ans += count * (count - 1) // 2
        return ans