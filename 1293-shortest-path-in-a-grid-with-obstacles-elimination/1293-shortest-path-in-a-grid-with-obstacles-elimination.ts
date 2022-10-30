function shortestPath(grid: number[][], k: number): number {
    let m = grid.length;
    let n = grid[0].length;
    let visited = new Array(m);
    for (let i = 0; i < m; i++) {
        visited[i] = new Array(n);
        for (let j = 0; j < n; j++) {
            visited[i][j] = new Array(k + 1).fill(false);
        }
    }
    let queue = [];
    queue.push([0, 0, k]);
    visited[0][0][k] = true;
    let step = 0;
    while (queue.length > 0) {
        let size = queue.length;
        for (let i = 0; i < size; i++) {
            let [x, y, remain] = queue.shift();
            if (x === m - 1 && y === n - 1) return step;
            for (let [dx, dy] of [[0, 1], [0, -1], [1, 0], [-1, 0]]) {
                let nx = x + dx;
                let ny = y + dy;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                    if (grid[nx][ny] === 0 && !visited[nx][ny][remain]) {
                        visited[nx][ny][remain] = true;
                        queue.push([nx, ny, remain]);
                    } else if (grid[nx][ny] === 1 && remain > 0 && !visited[nx][ny][remain - 1]) {
                        visited[nx][ny][remain - 1] = true;
                        queue.push([nx, ny, remain - 1]);
                    }
                }
            }
        }
        step++;
    }
    return -1;
};