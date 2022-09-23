class Solution {
    public int findCircleNum(int[][] C) {
        int N=C.length;
        int []v=new int[N];
        int c=0;
        for(int i=0;i<N;i++){
            if(v[i]==0){
                dfs(C,v,i);
                c++;
            }
        }
        return c;
    }
    private void dfs(int[][] C,int []v,int P){
        for(int j=0;j<C.length;j++){
            if(C[P][j]==1 && v[j]==0){
                v[j]=1;
                dfs(C,v,j);
            }
        }
    }
}