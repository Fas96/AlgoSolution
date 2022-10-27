function largestOverlap(img1: number[][], img2: number[][]): number {
     const n = img1.length;
    const count = new Map();
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (img1[i][j] === 1) {
                for (let i2 = 0; i2 < n; i2++) {
                    for (let j2 = 0; j2 < n; j2++) {
                        if (img2[i2][j2] === 1) {
                            const key = `${i - i2},${j - j2}`;
                            count.set(key, (count.get(key) || 0) + 1);
                        }
                    }
                }
            }
        }
    }
    return Math.max(...count.values(), 0);

};