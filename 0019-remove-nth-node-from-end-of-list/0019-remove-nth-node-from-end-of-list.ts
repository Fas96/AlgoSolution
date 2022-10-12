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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let dummy = new ListNode(0, head);
    let goUptoN = head;
    let JumpN = dummy;
    for (let i = 0; i < n; i++) {
        goUptoN = goUptoN.next;
    }
    while (goUptoN != null) {
        goUptoN = goUptoN.next;
        JumpN = JumpN.next;
    }
    JumpN.next = JumpN.next.next;
    return dummy.next;
};