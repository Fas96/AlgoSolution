class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                ans.append(asteroid)
            else:
                while ans and ans[-1] > 0 and ans[-1] < -asteroid:
                    ans.pop()
                if not ans or ans[-1] < 0:
                    ans.append(asteroid)
                elif ans[-1] == -asteroid:
                    ans.pop()
                    
        return ans