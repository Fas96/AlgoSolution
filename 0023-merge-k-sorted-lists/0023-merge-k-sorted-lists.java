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
    public ListNode mergeKLists(ListNode[] lists) {
           PriorityQueue<ListNode> pq=new PriorityQueue<>((a,b)->a.val-b.val);
        for (ListNode list : lists) {
            if(list!=null) pq.add(list);
        }
        ListNode tmp=new ListNode(-1);
        ListNode cur=tmp;
        while(!pq.isEmpty()){
            ListNode poll = pq.poll();
            cur.next=poll;
            cur=cur.next;
            if(poll.next!=null) pq.add(poll.next);
        }
        return tmp.next;
    }
}