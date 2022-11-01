function findBall(grid: number[][]): number[] {
   let result = [];
    for (let i = 0; i < grid[0].length; i++) {
        let x = 0;
        let y = i;
        while (x < grid.length) {
            if (grid[x][y] === 1) {
                if (y === grid[0].length - 1 || grid[x][y + 1] === -1) {
                    result.push(-1);
                    break;
                } else {
                    y++;
                }
            } else {
                if (y === 0 || grid[x][y - 1] === 1) {
                    result.push(-1);
                    break;
                } else {
                    y--;
                }
            }
            x++;
        }
        if (x === grid.length) {
            result.push(y);
        }
    }
    return result;
};