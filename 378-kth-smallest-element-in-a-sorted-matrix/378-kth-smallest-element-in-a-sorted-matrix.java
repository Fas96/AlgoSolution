class Solution {
    public int kthSmallest(int[][] matrix, int k) {
       List<Integer> A=new ArrayList<>();

        for (int []a:matrix) {
             A.addAll(Arrays.stream(a).boxed().collect(Collectors.toList()));
        }
        Collections.sort(A);
        return A.get(k-1);
    }
}