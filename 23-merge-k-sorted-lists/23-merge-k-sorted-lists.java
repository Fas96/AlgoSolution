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
       PriorityQueue<Integer> ans = new PriorityQueue<Integer>();
   
        for (ListNode ls:lists) {
           
            while (ls!=null){
                int val=ls.val;
                ls=ls.next;
                ans.add(val);
            }
        }
        ListNode lsAns= new ListNode(-1);
        ListNode d=lsAns;
        while(!ans.isEmpty()){
            int val=ans.poll();
            ListNode n=new ListNode(val);
            d.next=n;
            d=d.next;
        }
        return  lsAns.next;
    }
}