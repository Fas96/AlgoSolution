class Solution {
 private boolean isUnique(String s){
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i)-'a']++;
            if(count[s.charAt(i)-'a']>1){
                return false;
            }
        }
        return true;

    }

    public int maxLength(List<String> arr) {
        int[] res = new int[1];
        dfs(arr,0,"",res);
        return res[0];
    }

    private void dfs(List<String> arr, int i, String s, int[] res) {
        if(i==arr.size()){
            if(isUnique(s)){
                res[0]=Math.max(res[0],s.length());
            }
            return;
        }
        dfs(arr,i+1,s,res);
        dfs(arr,i+1,s+arr.get(i),res);
    }
}