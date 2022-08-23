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
    public boolean isPalindrome(ListNode head) {
        ListNode cur=head;
        
        if(cur==null)return false;
        List<Integer> k=new ArrayList<>();
        while(cur!=null){
             k.add(cur.val);
            cur=cur.next;
           
        }
       
        for(int i=0;i<k.size();i++){
            if(k.get(i)!=k.get(k.size()-i-1)) return false;
        } 
        
        return true;
    }
}