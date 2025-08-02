from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter(basket1)
        freq.subtract(Counter(basket2))

        to_swap = []
        for fruit_cost, count in freq.items():
            if count % 2 != 0:
                return -1
            for _ in range(abs(count) // 2):
                to_swap.append(fruit_cost)

        to_swap.sort()
        min_overall_fruit = min(basket1 + basket2)
        cost = 0

        for i in range(len(to_swap) // 2):
            direct_swap = to_swap[i]
            indirect_swap = min_overall_fruit * 2
            cost += min(direct_swap, indirect_swap)

        return cost