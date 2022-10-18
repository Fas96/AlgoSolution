function dfs(isConnected: number[][], visited: any[], i: number) {
    for (let j = 0; j < isConnected.length; j++) {
        if (isConnected[i][j] == 1 && !visited[j]) {
            visited[j] = true;
            dfs(isConnected, visited, j);
        }
    }
}

function findCircleNum(isConnected: number[][]): number {
    let visited = new Array(isConnected.length);
    let count = 0;
    for (let i = 0; i < isConnected.length; i++) {
        if (!visited[i]) {
            dfs(isConnected, visited, i);
            count++;
        }
    }
    return count;

};