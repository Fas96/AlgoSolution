class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        ROWS = len(maze)
        COLS = len(maze[0])

        visit = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        

        minHeap = [(0, start[0], start[1])]
        while minHeap:
            cost, row, col = heapq.heappop(minHeap)
            if (row, col) in visit:continue
            visit.add((row, col))

            if row == destination[0] and col == destination[1]:
                return cost
            for r, c in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                R, C,k = row,col,0
                while 0<=R<ROWS and 0<=C< COLS and maze[R][C] == 0: 
                    R += r
                    C += c
                    k+=1
                R-=r
                C-=c
                k-=1
                if (R, C) not in visit: 
                    heapq.heappush(minHeap, (cost + k, R, C))
        
        return -1
        