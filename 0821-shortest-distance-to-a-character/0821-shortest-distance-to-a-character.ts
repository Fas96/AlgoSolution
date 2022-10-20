function shortestToChar(s: string, c: string): number[] {

    
    let result: number[] = new Array(s.length);
    let prev: number = -1;
    for (let i = 0; i < s.length; i++) {
        if (s.charAt(i) == c) {
            result[i] = 0;
            prev = i;
        } else if (prev != -1) {
            result[i] = i - prev;
        } else {
            result[i] = Number.MAX_SAFE_INTEGER;
        }
    }
    prev = -1;
    for (let i = s.length - 1; i >= 0; i--) {
        if (s.charAt(i) == c) {
            prev = i;
        } else if (prev != -1) {
            result[i] = Math.min(result[i], prev - i);
        }
    }
    return result;
};