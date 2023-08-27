class UnionFind(object):
    def __init__(self, grid):
        row, col = len(grid), len(grid[0])
        self.parent = ['w'] * (row * col)
        self.count = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    self.parent[(col * r) + c] = -1
    
    def find(self, index):
        if self.parent[index] == 'w':
            return index
        
        if self.parent[index] > -1:
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]
        
        return index
    
    def union(self, vertexA, vertexB):
        aIndex = self.find(vertexA)
        bIndex = self.find(vertexB)

        if aIndex == bIndex or self.isWater(aIndex, bIndex):
            return
        
        if self.parent[aIndex] > self.parent[bIndex]:
            self.parent[bIndex] += self.parent[aIndex]
            self.parent[aIndex] = bIndex
        else:
            self.parent[aIndex] += self.parent[bIndex]
            self.parent[bIndex] = aIndex
    
    def isWater(self, aIndex, bIndex):
        return self.parent[aIndex] == 'w' or self.parent[bIndex] == 'w'
		
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        uf = UnionFind(grid)

        for r in range(row):
            for c in range(col):
                
                if grid[r][c] is '1':
                    parentIndex = (col * r) + c

                    # right
                    if c < col - 1:
                        right = parentIndex + 1
                        uf.union(parentIndex, right)
                    
                    # down
                    if r < row - 1:
                        down = (col * (r+1)) + c
                        uf.union(parentIndex, down)
        
        islands = 0
        for ele in uf.parent:
            if ele is not 'w' and ele < 0:
                islands +=1

        return islands