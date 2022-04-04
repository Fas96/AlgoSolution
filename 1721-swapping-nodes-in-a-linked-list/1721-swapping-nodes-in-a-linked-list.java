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
    public ListNode swapNodes(ListNode head, int k) {
            
            ListNode tmp= head;
         Map<Integer,ListNode> kepItems= new HashMap<>();
            int totalNodes=1;
            while(tmp!=null) {
                kepItems.put(totalNodes,tmp);
                totalNodes++;
                tmp=tmp.next;
            }
            int start=kepItems.get(k).val;
            kepItems.get(k).val=kepItems.get(totalNodes-k).val;
            kepItems.get(totalNodes-k).val=start;
            
            return head;
       
    }
}