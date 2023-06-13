class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        num = 0
        for c in range(len(grid)):
            temp = []
            for r in range(len(grid[c])):
                temp.append(grid[r][c])   
            num+= grid.count(temp)
        return num