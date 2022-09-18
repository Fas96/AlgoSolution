class Solution {
    public int trap(int[] height) {
    int N=height.length;
    if(N<3)return 0;
    int[]left=new int[N];
    for (int i = 0; i < N; i++) {
      left[i]=i==0?height[i]:Math.max(left[i-1],height[i]);
    }
    System.out.println();
    int[]right=new int[N];
    for (int i = N-1; i >=0 ; i--) {
      right[i]=i==N-1?height[i]:Math.max(right[i+1],height[i]);
    }
    int sum=0;
    for (int i = 0; i < N; i++) {
      sum+=Math.min(left[i],right[i] )-height[i];
    }
    return sum;
    }
}

// 1*(2-1) 
// 2*(4)-2
// 1
    