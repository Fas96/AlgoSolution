/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
       if(head==null) return null;
        
        ListNode curNode=head;
        ArrayList<ListNode> list=new ArrayList<>();
         
        while(curNode!=null){
            if(list.contains(curNode)){
                return curNode;
            }
            list.add(curNode);
            curNode=curNode.next;
        }
        return null; 
    }
}