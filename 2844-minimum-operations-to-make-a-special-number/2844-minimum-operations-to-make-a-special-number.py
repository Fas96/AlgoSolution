class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        
        @cache
        def bactrack(index, current):
            if index == n:
                return 0 if current == 0 else float('inf')
            return  min(bactrack(index + 1, (10 * current + int(num[index])) % 25), bactrack(index + 1, current) + 1) 
        return bactrack(0, 0)
        