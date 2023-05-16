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
    public ListNode swapPairs(ListNode head) {
        ListNode node = head;
        ListNode prev = null;
        while (node != null && node.next != null) {
            ListNode next = node.next;
            node.next = next.next;
            next.next = node;

            if (prev == null) {
                head = next;
            } else {
                prev.next = next;
            }
            prev = node;
            node = node.next;
        }
        return head;
    }
}