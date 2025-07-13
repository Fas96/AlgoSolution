class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        ipx,matchCount,N=0,0,len(trainers)
        for p in players:
            while ipx<N and  p>trainers[ipx]:
                ipx+=1
            if ipx<N:
                ipx+=1
                matchCount+=1
        return matchCount
        