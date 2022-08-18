/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 
 Ctr+C: review later
 */
class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] answer = new int[m][n];
        for (int[] ints : answer) {
            Arrays.fill(ints, -1);
        }

        int y = 0;
        int x = 0;
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int curDir = 0;
        int cnt = 0;
        while (head != null) {
            answer[y][x] = head.val;

            if (++cnt == m * n) {
                return answer;
            }

            int[] dir = dirs[curDir];
            int nextY = y + dir[0];
            int nextX = x + dir[1];
            if (nextY < 0 || nextY >= m || nextX < 0 || nextX >= n || answer[nextY][nextX] != -1) {
                curDir = (curDir + 1) % 4;
                nextY = y + dirs[curDir][0];
                nextX = x + dirs[curDir][1];
            }
            y = nextY;
            x = nextX;
            head = head.next;
        }
        return answer;
    }
}