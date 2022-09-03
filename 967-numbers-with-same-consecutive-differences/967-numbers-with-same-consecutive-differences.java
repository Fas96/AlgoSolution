class Solution {
    public int[] numsSameConsecDiff(int n, int k) {
    List<Integer> listNums= new ArrayList<>();
    if(n==0)return new int[0];
    dfs(n,k,listNums,0);
    return listNums.stream().mapToInt(e->e).toArray();
  }

  private void dfs(int n, int k, List<Integer> listNums,int genNum) {
    if(n==0){listNums.add(genNum);return;}
    for (int i = 0; i < 10; i++) {
      if(i==0 && genNum==0) continue;
      if(genNum==0){
        dfs(n-1, k, listNums, i);
      }
      else if(Math.abs((genNum%10) - i )==k) {
        dfs(n - 1, k, listNums, genNum * 10 + i);
      }
    }
  }
}