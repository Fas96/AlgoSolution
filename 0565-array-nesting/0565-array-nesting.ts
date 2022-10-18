function arrayNesting(nums: number[]): number {
let max = 0;
    for (let i = 0; i < nums.length; i++) {
        let count = 0;
        let j = i;
        while (nums[j] != -1) {
            let temp = nums[j];
            nums[j] = -1;
            j = temp;
            count++;
        }
        max = Math.max(max, count);
    }
    return max;
};