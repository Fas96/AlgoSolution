class Solution {
     public List<Integer> multiply(List<Integer> num1, List<Integer> num2) {
       final  int sign= num1.get(0) < 0 ^ num2.get(0) < 0 ? -1 : 1;

         num1.set(0, Math.abs(num1.get(0)));
         num2.set(0, Math.abs(num2.get(0)));
         
         List<Integer> result = new ArrayList<>(Collections.nCopies(num1.size() + num2.size(), 0));
            for (int i = num1.size() - 1; i >= 0; --i) {
                for (int j = num2.size() - 1; j >= 0; --j) {
                    result.set(i + j + 1, result.get(i + j + 1) + num1.get(i) * num2.get(j));
                    result.set(i + j, result.get(i + j) + result.get(i + j + 1) / 10);
                    result.set(i + j + 1, result.get(i + j + 1) % 10);
                }
            }
            int firstNotZero = 0;
            while (firstNotZero < result.size() && result.get(firstNotZero) == 0) {
                ++firstNotZero;
            }
            result = result.subList(firstNotZero, result.size());
            if (result.isEmpty()) {
                return Collections.singletonList(0);
            }
            result.set(0, result.get(0) * sign);
            return result;
    }

    public String multiply(String num1, String num2) {
        List<Integer> numInt1, numInt2;
        numInt1 = new ArrayList<>();
        numInt2 = new ArrayList<>();
        for (int i = 0; i < num1.length(); i++) {
            numInt1.add(num1.charAt(i) - '0');
        }
        for (int i = 0; i < num2.length(); i++) {
            numInt2.add(num2.charAt(i) - '0');
        }
        List<Integer> result = multiply(numInt1, numInt2);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i));
        }
        return sb.toString();
    }
}