class Solution {
  List<Integer> flatten2DList(List<List<Integer>> listOfLists){
    return   listOfLists.stream().collect(ArrayList::new, List::addAll, List::addAll);
  }
  public int kthSmallest(int[][] matrix, int k) {
    List<List<Integer>> acc= new ArrayList<>();
    for (int[] l : matrix) {
      acc.add( Arrays.stream(l).boxed().collect(Collectors.toList()));
    }
    List<Integer> flatten2DList = flatten2DList(acc).stream().sorted().collect(Collectors.toList());

 
    return  flatten2DList.get(k-1);
  }
}