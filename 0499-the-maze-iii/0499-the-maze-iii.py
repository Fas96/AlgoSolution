class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        ROWS = len(maze)
        COLS = len(maze[0])

        visit = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        Maps = {(0, 1): "r", (0, -1): "l", (1, 0): "d", (-1, 0): "u"}

        pQ = [(0, ball[0], ball[1], "")]
        while pQ:
            cost, row, col, path = heapq.heappop(pQ)
            if (row, col) in visit:
                continue
            visit.add((row, col))
            if [row, col] == hole:
                return path

            for dRow, dCol in directions:
                R = row
                C = col
                k = 0
                while 0 <= R + dRow < ROWS and 0 <= C + dCol < COLS and maze[R + dRow][C + dCol] == 0:
                    if [R, C] == hole:
                        break
                    k += 1
                    R = R + dRow
                    C = C + dCol
                if (R, C) not in visit:
                    p = Maps[(dRow, dCol)]
                    heapq.heappush(pQ, (cost + k, R, C, path + p))

        return "impossible"
        