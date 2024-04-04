# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dd=head
        dum=ListNode(-1)
        cur=dum
        while dd:
            if dd.val==val:
                dd=dd.next
                continue
            cur.next=ListNode(dd.val)
            cur=cur.next
            dd=dd.next
            
        return dum.next