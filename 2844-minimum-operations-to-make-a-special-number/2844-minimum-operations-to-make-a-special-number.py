class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num) 
        @cache
        def pick(index, current):
            if index == n:
                return 0 if current == 0 else float('inf')
            return  min(pick(index + 1, (10 * current + int(num[index])) % 25), pick(index + 1, current) + 1) 
        return pick(0, 0)
        