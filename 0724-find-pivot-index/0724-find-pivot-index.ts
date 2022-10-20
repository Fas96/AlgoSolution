function pivotIndex(nums: number[]): number {

    let sum: number = 0;
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
    }
    let left: number = 0;
    for (let i = 0; i < nums.length; i++) {
        if (left == sum - left - nums[i]) {
            return i;
        }
        left += nums[i];
    }
    return -1;
};