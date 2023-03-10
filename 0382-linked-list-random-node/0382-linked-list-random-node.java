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

    ArrayList<ListNode> listNodeArrayList;
    public Solution(ListNode head) {
        if (head==null)return;
        ListNode  curNode=head;
         listNodeArrayList=new ArrayList<>();
        while(curNode!=null){
            listNodeArrayList.add(curNode);
            curNode=curNode.next;
        }
    }

    public int getRandom() {
        Random rand = new Random();
        int randomIndex = rand.nextInt(listNodeArrayList.size());
        return listNodeArrayList.get(randomIndex).val;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */