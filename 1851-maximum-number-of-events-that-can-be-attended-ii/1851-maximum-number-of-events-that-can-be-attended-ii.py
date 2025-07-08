class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [i for i, _, _ in events]
        
        @cache
        def fn(i, k): 
            """Return max score of attending k events from events[i:]."""
            if i == len(events) or k == 0: return 0 
            ii = bisect_left(starts, events[i][1]+1)
            return max(fn(i+1, k), events[i][2] + fn(ii, k-1))
        
        return fn(0, k)