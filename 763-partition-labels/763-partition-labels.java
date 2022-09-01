class Solution {
    public List<Integer> partitionLabels(String s) {
        char[] arr=s.toCharArray();
    int[] cache= new int[128];
    for (int i = 0; i < arr.length; i++) {
      cache[arr[i]]=i;
    }
    int L=0,R=0,index=0;
    List<Integer> res= new LinkedList<>();
    while (index<arr.length){
      char cur=arr[index];
      R=Math.max(R,cache[cur]);
      if(R==index){
        int size=R-L+1;
        res.add(size);
        R++;
        L=R;
      }
      index++;
    }
    return res;
    }
}