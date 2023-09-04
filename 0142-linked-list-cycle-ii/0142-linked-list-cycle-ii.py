# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        seen=set()
        while head:
            if head not in seen:
                seen.add(head)
            else:
                return head
            head=head.next
        return None
        