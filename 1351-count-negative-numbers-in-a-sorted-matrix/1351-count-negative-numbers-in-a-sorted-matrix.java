class Solution {
    public int countNegatives(int[][] grid) {
               return (int) Arrays.stream(Stream.of(grid)  
                .flatMapToInt(IntStream::of)  
                .toArray()).filter(e->e<0).count();
    }
}