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
    public ListNode oddEvenList(ListNode head) {
         if(head==null||head.next==null) return head;
        List<ListNode> odd=new LinkedList<>();
        List<ListNode> even=new LinkedList<>();
        ListNode temp=head;
        int i=1;
        while(temp!=null){
            if(i%2==0){
                even.add(temp);
            }else{
                odd.add(temp);
            }
            i++;
            temp=temp.next;
        }
        ListNode oddHead=odd.get(0);
        ListNode evenHead=even.get(0);
        
        ListNode oddTemp=oddHead;
        ListNode evenTemp=evenHead;
        
        for (int j = 1; j < odd.size(); j++) {
            oddTemp.next=odd.get(j);
            oddTemp=oddTemp.next;
        }
        for (int j = 1; j < even.size(); j++) {
            evenTemp.next=even.get(j);
            evenTemp=evenTemp.next;
        }
        oddTemp.next=evenHead;
        evenTemp.next=null;
        return oddHead;
    }
}