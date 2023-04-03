class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int result = 0;
        int n = people.length;
        int i = 0, j = n - 1;
        while (i <= j) {
            if (people[i] + people[j] <= limit) {
                i++;
            }
            j--;
            result++;
        }
        return result;
    }
}