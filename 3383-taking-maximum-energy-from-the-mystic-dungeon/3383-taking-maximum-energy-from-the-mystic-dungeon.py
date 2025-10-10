class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        t=energy 
        n=len(energy)
        for i in range(n-1,-1,-1): #traverse backwards
            if i+k<n: #when there is a next jump
                t[i]=energy[i]+t[i+k] #if jump exist, update current
        return max(t) #the max after jumps aggregation added
        