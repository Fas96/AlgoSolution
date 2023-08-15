# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        initialDir=cur=ListNode(-1)
        secondDir=cur1=ListNode(-2)
        
        while head:
            if head.val<x:
                initialDir.next=head
                initialDir=initialDir.next
            else:
                secondDir.next=head
                secondDir=secondDir.next
            head=head.next
        secondDir.next=None
        initialDir.next=cur1.next
        return cur.next
        