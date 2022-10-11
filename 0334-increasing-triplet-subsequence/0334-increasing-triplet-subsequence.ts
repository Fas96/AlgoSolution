function binarySearch(dp: any[], number: number, len: number, num: number): number {
    let left = number;
    let right = len;
    while (left < right) {
        let mid = Math.floor((left + right) / 2);
        if (dp[mid] < num) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
    
}

function increasingTriplet(nums: number[]): boolean {
    let n = nums.length;
    let dp = new Array(n).fill(0);
    let len = 0;
    for (let num of nums) {
        let i = binarySearch(dp, 0, len, num);
        dp[i] = num;
        if (i == len) len++;
    }

    return len >= 3;
};