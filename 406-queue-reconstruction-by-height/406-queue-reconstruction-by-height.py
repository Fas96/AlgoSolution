class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x: (-x[0],x[1]))
        lsL=[]
        # people = sorted(people, key = lambda x: (-x[0], x[1]))
        # print([[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]])
        
        for k in people:
            lsL.insert(k[1],k)
        print(lsL)
        return lsL
        
        
            