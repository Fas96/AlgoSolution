function threeSumClosest(nums: number[], target: number): number {
  let gap:number=Number.MAX_SAFE_INTEGER;
    let ans:number=0;
    nums.sort((a,b)=>a-b);
    for(let i=0;i<nums.length-2;i++){
        let j=i+1;
        let k=nums.length-1;
        while(j<k){
            let sum=nums[i]+nums[j]+nums[k];
            if(sum==target){
                return target;
            }
            if(Math.abs(sum-target)<gap){
                gap=Math.abs(sum-target);
                ans=sum;
            }
            if(sum<target){
                j++;
            }else{
                k--;
            }
        }
    }
    
    return ans;
};