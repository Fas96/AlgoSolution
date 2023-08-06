class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        songComb={}
        MOD=10**9+7
        
        def songc(idx,jdx):
            
            if (idx,jdx) in songComb:
                return songComb[idx,jdx]
            
            if idx == 0:
                songComb[idx,jdx]=(jdx==0)
                return songComb[idx,jdx]
            
            
            curRepeats=songc(idx-1, jdx) * ( jdx - k ) if jdx > k else 0 
            curUnique=songc(idx-1, jdx-1)*(n-(jdx-1))
             
            songComb[idx,jdx]=(curRepeats+curUnique)%(MOD)
            
            return songComb[idx,jdx]
            
        return songc(goal,n)
        
        