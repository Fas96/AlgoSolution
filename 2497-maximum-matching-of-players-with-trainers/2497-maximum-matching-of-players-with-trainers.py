class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        j=0
        ans=0
        n=len(trainers)
        for i, p1 in enumerate(players):
            while j<n and trainers[j]<p1: j+=1
            if j<n:
                j+=1
                ans+=1 
        return ans
        