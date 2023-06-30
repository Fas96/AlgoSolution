class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        parents = {}

        def ufind(key):
            if parents[key] != key:
                parents[key] = ufind(parents[key])
            return parents[key]

        def uunion(a, b):
            pa = ufind(a)
            pb = ufind(b)
            parents[pa] = pb

        for x in range(row):
            for y in range(col):
                parents[(x, y)] = (x, y)
        left = -1
        right = -2

        parents[left] = left
        parents[right] = right
 
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        seen = set()
        for t, (x, y) in enumerate(cells):
            x -= 1
            y -= 1
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx <row:
                    if 0 <= ny < col:
                        if (nx, ny) in seen:
                            uunion((x, y), (nx, ny))
                    else:
                        if ny == -1:
                            uunion((x, y), left)
                        if ny == col:
                            uunion((x, y), right)
                if ufind(left) == ufind(right):
                    return t
                seen.add((x, y))
        return -1