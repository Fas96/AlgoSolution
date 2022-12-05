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
    public ListNode middleNode(ListNode head) {
        List<ListNode> list = new LinkedList<>();
        ListNode slow = head; 
        while (slow != null) {
            list.add(slow);
            slow = slow.next;
        }
        return list.get(list.size()/2);
    }
}