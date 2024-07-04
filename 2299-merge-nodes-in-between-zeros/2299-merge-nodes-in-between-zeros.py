# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = res = ListNode()
        csum = 0
        
        while head:
            if head.val != 0:
                csum += head.val
            elif head.val==0 and csum>0:
                cur.next = ListNode(csum)
                cur = cur.next
                csum = 0
            head=head.next
 
        
        return res.next
        