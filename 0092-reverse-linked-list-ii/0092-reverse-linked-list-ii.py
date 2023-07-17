# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nodes= []
        while head:
            nodes.append(head.val)
            head = head.next
        nodes[left-1:right] = nodes[left-1:right][::-1]
        dummy = ListNode()
        cur = dummy
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return dummy.next
        