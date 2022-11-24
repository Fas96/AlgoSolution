/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
   var mx=-82737283;
    var glbx=0;
    
    for(var x of nums){
        glbx=Math.max(glbx+x,x);
        mx=Math.max(mx,glbx);
    }
    
    return mx;
    
};

 
 
