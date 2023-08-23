class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        ROWS = len(maze)
        COLS = len(maze[0])

        visit = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        

        q = deque([(start[0], start[1])])
        while q:
            row, col= q.popleft()

            if (row, col) in visit:continue
            visit.add((row, col))

            if row== destination[0] and col== destination[1]:  return True
            for i, j in (-1, 0) , (1, 0), (0, -1), (0, 1):
                R, C = row, col
                while 0 <= R< ROWS and 0 <= C< COLS and maze[R][C] == 0:
                    R += i
                    C += j  
                R-=i
                C-=j
                if (R, C) not in visit:
                     q.append((R, C))
        return False
        