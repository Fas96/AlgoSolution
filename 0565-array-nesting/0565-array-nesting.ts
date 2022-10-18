function arrayNesting(nums: number[]): number {
    // let max = 0;
    // for (let i = 0; i < nums.length; i++) {
    //     let count = 0;
    //     let j = i;
    //     //checking the sets that can be stacked over each other by the index
    //     while (nums[j] != -1) {
    //         let temp = nums[j];
    //         //we made nums[j] -1 so that we dont visit it again in the loop
    //         nums[j] = -1;
    //         //j goes to the next index if it was not already visited
    //         j = temp;
    //         //count if the loop continues
    //         count++; 
    //     }
    //     max = Math.max(max, count);
    // }
    // return max;
      let mx=0;
    for (let i = 0; i < nums.length; i++) {
        let cnt=0;
        let j=i;
        while (nums[j]!=-1){
            let temp=nums[j]
            nums[j]=-1
            j=temp;
            cnt++;
        }
        mx=Math.max(mx,cnt)
    }
    
    return mx;
};