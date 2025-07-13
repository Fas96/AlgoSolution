class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        i=0
        ans=0
        n=len(trainers)
        for p in players:
            while i<n and  p>trainers[i]:
                i+=1
            if i<n:
                i+=1
                ans+=1
        return ans
        