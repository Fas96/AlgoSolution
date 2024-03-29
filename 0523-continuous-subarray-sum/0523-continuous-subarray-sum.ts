function checkSubarraySum(nums: number[], k: number): boolean {

    const map = new Map();
    map.set(0, -1);
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        if (k !== 0) {
            sum %= k;
        }
        if (map.has(sum)) {
            if (i - map.get(sum) > 1) {
                return true;
            }
        } else {
            map.set(sum, i);
        }
    }
    return false;
};