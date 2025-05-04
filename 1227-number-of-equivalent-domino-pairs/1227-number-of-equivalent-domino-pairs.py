class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_counts = defaultdict(int)
        for domino in dominoes:
            normalized = tuple(sorted(domino))
            domino_counts[normalized] += 1
        
        total_pairs = 0
        for count in domino_counts.values():
            if count >= 2:
                total_pairs += count * (count - 1) // 2
        return total_pairs