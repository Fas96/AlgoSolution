class Solution {
   public int[] findOriginalArray(int[] changed) {
       int N=changed.length/2;
  int[] temp = new int[N];
    Queue<Integer> x = new LinkedList<>();
    Arrays.sort(changed);
    int i = 0;
    for(int num : changed){
        if(!x.isEmpty() && x.peek()==num)
            temp[i++] = x.poll()/2;
        else x.add(num*2);
    }
    return x.size()>0 ? new int[]{}:temp;
   }
        
//     public int[] findOriginalArray(int[] changed) {
//         int L=0,R=0,P=0,N=changed.length;
//         List<Integer> res= new ArrayList<>();
//         if(N<2)return new int[]{};
//         while (R<N){
//             if(changed[L]*2==changed[R] && changed[L]!=changed[R]){
//                 res.add(changed[L]);
//                 L++;
//             }else if(changed[L]==changed[R] && changed[L]==0){
//                 P++;
//             }
//             R++;
//         }
//         int[] array=null;

//         if(verifyAllEqualUsingHashSet(changed)&& P>0){
//             array=new int[(int)P/2];
//             for (int i = 0; i < array.length; i++) {
//                 array[i]=changed[i];
//             }
            
//             return array;
//         }
//           array = new int[res.size()];
//         for (int i = 0; i < array.length; i++) {
//             array[i]=res.get(i);
//         }
//         return   array;
//     }

//     public boolean verifyAllEqualUsingHashSet(int[] arr) {
//         Set<Integer> distinct = Arrays.stream(arr).boxed().collect(Collectors.toSet());
//         boolean allEqual = distinct.size() <= 1;
//        return allEqual;
//     }
}