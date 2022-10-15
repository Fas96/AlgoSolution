/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

 

function reverse(start: ListNode) {
        let prev = null;
        let curr = start;
        while (curr) {
            let next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
  }

    function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    let dummy = new ListNode(0);
    dummy.next = head;
    let prev = dummy;
    let end = dummy;
    while (end.next != null) {
        for (let i = 0; i < k && end != null; i++) end = end.next;
        if (end == null) break;
        let start = prev.next;
        let next = end.next;
        end.next = null;
        prev.next = reverse(start);
        start.next = next;
        prev = start;
        end = prev;
    }
    return dummy.next;

};