class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:  
    
        total = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set() # Initiate hashset
        
        
		# 1. Iterate over grid and find starting position and total no. of keys.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    start = (i, j)
                if grid[i][j] in 'abcdef':
                    total += 1
        
        queue = [(start[0], start[1], tuple(), 0)] # Initiate queue using list of tuples, add starting position to queue (row, col, set(keys), no. of moves)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # can either move up, down, left or right
        
        while queue:
            i, j, keys, moves = queue.pop(0)   
            if (i, j, keys) not in visited: # only check if that position has not already been visited whilst we have the same collection of keys.
                visited.add((i, j, keys))   # add combination to set     
                if len(set(keys)) == total: # if no of keys we have obtained is equal to total then we have found the minimum number of moves.
                    return moves
                
                for x, y in directions:
                    new_keys = set(keys) # create set from tuple so we can easily compare if we have key for lock we may encounter
                    row, col = i + x, j + y # new coordinates
                    if row >= 0 and col >= 0 and row < ROWS and col < COLS and grid[row][col] != '#': # if the row and column is in range of grid and not a wall.
                        if grid[row][col] in 'ABCDEF' and grid[row][col].lower() not in new_keys:
                            continue # then we do not have the key for this lock and cannot pass
                        if grid[row][col].islower() and grid[row][col] != '.':
                            new_keys.add(grid[row][col]) # obtained a new key and add to queue
                            queue.append((row, col, tuple(new_keys), moves+1))

                        else:
                            queue.append((row, col, tuple(new_keys), moves+1)) # havent obtained a new key but is a valid move

        return -1 