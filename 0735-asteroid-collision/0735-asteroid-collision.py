class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        for asteroid in asteroids:
            while ans and asteroid<0<ans[-1]:
                if ans[-1]<-asteroid:
                    ans.pop()
                    continue
                elif ans[-1]==-asteroid:
                    ans.pop()
                break
            else:
                ans.append(asteroid)
        return ans