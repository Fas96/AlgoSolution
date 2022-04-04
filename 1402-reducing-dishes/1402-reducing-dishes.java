class Solution {
    public int maxSatisfaction(int[] satisfaction) {
              int[] ints = Arrays.stream(satisfaction).sorted().toArray();
            int[] coefficient = new int[ints.length];
            for (int i = 0; i < coefficient.length; i++) {
                coefficient[i]=i+1;
            }
            int max=-0;
            int reduc=0;
            for (int i = 0; i < ints.length; i++) {
                int innerSUm=0;

                for (int j = i; j < ints.length; j++) {
                    innerSUm+=(ints[j]*coefficient[j-reduc]);
                }
                reduc++;
                max=Math.max(max,innerSUm);
            }

            return max;
        
    }
}