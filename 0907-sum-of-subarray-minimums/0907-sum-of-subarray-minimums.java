class Solution {
    public int sumSubarrayMins(int[] arr) {
      long sum = 0;
        Stack<Integer> stack = new Stack<> ();
        for (int i = 0; i <= arr.length; i++) {
            while (!stack.isEmpty() && (i == arr.length || arr[stack.peek()] > arr[i])) {
                int pop = stack.pop(), prev = stack.isEmpty() ? -1 : stack.peek();
                sum += (pop - prev) * (i - pop) * (long)arr[pop];
            }
            stack.push(i);
        }
        return (int)(sum % (Math.pow(10,9) + 7));
    }
}