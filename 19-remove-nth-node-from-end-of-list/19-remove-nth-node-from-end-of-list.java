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
    public ListNode removeNthFromEnd(ListNode head, int n) {
           List<ListNode> getList= new LinkedList<>();
          ListNode temp=head;
          while (temp!=null){
              getList.add(temp);
              temp=temp.next;
          }
            System.out.println(getList);
           int index=getList.size()-n;
            if (index==0){
                head=head.next;
            }else {
                getList.get(index-1).next=getList.get(index).next;
            }
            return head;
    }
}