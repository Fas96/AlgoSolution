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
    public void reorderList(ListNode head) {
         if(head==null||head.next==null) return;
        
            ListNode slow = head, fast = head;
            while (fast != null && fast.next != null) {
                fast = fast.next.next;
                slow = slow.next;
            }
            ListNode headSecondHalf = reverse(slow);
            ListNode headFirstHalf = head;
            while (headFirstHalf != null && headSecondHalf != null) {
                ListNode temp = headFirstHalf.next;
                headFirstHalf.next = headSecondHalf;
                headFirstHalf = temp;

                temp = headSecondHalf.next;
                headSecondHalf.next = headFirstHalf;
                headSecondHalf = temp;
            }
            if (headFirstHalf != null) {
                headFirstHalf.next = null;
            }
        }
    

    private ListNode reverse(ListNode slow) {
        ListNode prev=null,cur=slow;
        while(cur!=null){
            ListNode next=cur.next;
            cur.next=prev;
            prev=cur;
            cur=next;
        }
        return prev;
    }
}