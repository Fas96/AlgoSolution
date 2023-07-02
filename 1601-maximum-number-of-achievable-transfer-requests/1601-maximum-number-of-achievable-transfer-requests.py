class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:   
        l = len(requests)
        buildings = [0 for i in range(n)]
        self.res = 0

        def recur(index,cur,buildings):
            if all(e==0 for e in buildings):
                self.res = max(self.res,cur)
            if index == len(requests):
                return
            
            for i in range(index,l):
                src,dest = requests[i]
                buildings[src] -= 1
                buildings[dest] += 1

                recur(i+1,cur+1,buildings)

                buildings[src] += 1
                buildings[dest] -= 1
        
        recur(0,0,buildings)
        return self.res

        