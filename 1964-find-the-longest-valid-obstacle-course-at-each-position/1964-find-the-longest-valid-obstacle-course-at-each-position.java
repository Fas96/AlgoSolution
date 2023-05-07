class Solution {
    public int[] longestObstacleCourseAtEachPosition(int[] obstacles) {
        int n = obstacles.length;
        int[] ans = new int[n];
        List<Integer> list = new ArrayList<>();
        Arrays.fill(ans,1);
        ans[0] = 1;
        for (int i = 0; i < n; i++) {
             int idx=binaSearch(list,obstacles[i]);
                if(idx==list.size()){
                    list.add(obstacles[i]);
                }else{
                    list.set(idx,obstacles[i]);
                }
                ans[i]=idx+1;
        }
        return ans;


    }

    private int binaSearch(List<Integer> list, int obstacle) {
        int left = 0, right = list.size() - 1;
        while (left <= right) {
            int mid = (right - left) / 2 + left;
            if(list.get(mid)<=obstacle){
                left=mid+1;
            }else{
                right=mid-1;
            }
        }
        return left;
    }
}