# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead, acc = ListNode(next=head), 0
        nodeBySum = {
            acc: dummyHead,
        }
        while head:
            acc += head.val
            if acc in nodeBySum:
                cursor, temp = nodeBySum[acc].next, acc
                while cursor is not head:
                    temp += cursor.val
                    cursor = nodeBySum.pop(temp).next
                nodeBySum[acc].next = cursor.next
            else:
                nodeBySum[acc] = head
            head = head.next

        return dummyHead.next
        