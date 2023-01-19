class Solution {
   public List<Integer> plusOne(List<Integer> A) {
        List<Integer> B = new ArrayList<>(A);
        int n = B.size()-1;
        B.set(n , B.get(n) + 1);
        for (int i = n ; i > 0 && B.get(i) == 10; --i) {
            B.set(i, 0);
            B.set(i - 1, B.get(i - 1) + 1);
        }
        if (B.get(0) == 10) {

            B.set(0, 1);
            B.add(0 );
        }
        return B;
    }
    public int[] plusOne(int[] digits) {
        List<Integer> A = new ArrayList<>();
        for (int i = 0; i < digits.length; i++) {
            A.add(digits[i]);
        }
        List<Integer> B = plusOne(A);
        int[] res = new int[B.size()];
        for (int i = 0; i < B.size(); i++) {
            res[i] = B.get(i);
        }
        return res;

    }
}