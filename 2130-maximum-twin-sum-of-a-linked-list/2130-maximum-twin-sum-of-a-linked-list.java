/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {
        List<Integer> list = new java.util.ArrayList<>();
        ListNode node = head;
        while (node != null) {
            list.add(node.val);
            node = node.next;
        }
        int max = 0;
        int idx = 0;
        int idxEnd = list.size() - 1;
        while (idx < idxEnd) {
            max = Math.max(max, list.get(idx) + list.get(idxEnd));
            idx++;
            idxEnd--;
        }
        return max;
    }
}