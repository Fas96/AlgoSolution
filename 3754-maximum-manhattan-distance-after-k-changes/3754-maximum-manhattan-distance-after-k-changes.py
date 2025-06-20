class Solution:
    def maxDistance(self, s: str, k: int) -> int: 
        def best_for(good):
            score = 0
            bad   = 0
            best  = 0

            for ch in s:
                if ch in good:         
                    score += 1
                else:                
                    score -= 1
                    bad   += 1
 
                best = max(best, score + 2 * min(k, bad))

            return best
 
        return max(
            best_for({'N', 'E'}),   # x + y
            best_for({'N', 'W'}),   # -x + y
            best_for({'S', 'E'}),   # x - y
            best_for({'S', 'W'})    # -x - y
        )