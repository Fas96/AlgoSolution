class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        resource = 0
        for i in range(len(colors)):
            cdf = 0
            for j in range(len(colors)):
                if i != j and colors[i] != colors[j]:
                    cdf = abs(i - j)
            resource = max(resource, cdf)
            
        return resource