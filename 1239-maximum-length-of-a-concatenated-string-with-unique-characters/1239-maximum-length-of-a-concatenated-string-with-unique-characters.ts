function isUnique(s: string) {
    const set = new Set();
    for (const c of s) {
        if (set.has(c)) {
            return false;
        }
        set.add(c);
    }
    return true;
}

function maxLength(arr: string[]): number {
    let max = 0;
    const dfs = (index: number, str: string) => {
        if (index === arr.length) {
            max = Math.max(max, str.length);
            return;
        }
        if (isUnique(str + arr[index])) {
            dfs(index + 1, str + arr[index]);
        }
        dfs(index + 1, str);
    };
    dfs(0, '');
    return max;

};