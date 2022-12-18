class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
          int[] ans = new int[temperatures.length];
            Stack<Integer> stack = new Stack<>();

            for (int i = 0; i < temperatures.length; i++) {
                while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                    int j = stack.pop();
                    ans[j] = i - j;
                }
                stack.push(i);
            }

            return ans;
    }
}