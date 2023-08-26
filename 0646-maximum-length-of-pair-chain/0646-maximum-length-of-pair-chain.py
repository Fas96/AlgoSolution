class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sPairs=sorted(pairs, key=lambda x: x[1])
        prev=0
        nonOverlap=1
     
        for i in range(1,len(sPairs)):
            if sPairs[i][0]>sPairs[prev][1]: 
                nonOverlap+=1
                prev=i
        return nonOverlap
        