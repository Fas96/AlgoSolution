# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
   
   
        cs=0
        tail = dum = ListNode(-1)
        while head:
            if head.val==0 and cs>0: 
                tail.next = ListNode(cs)
                tail = tail.next
                cs=0
            cs+=head.val
            head=head.next
    
        return dum.next
        