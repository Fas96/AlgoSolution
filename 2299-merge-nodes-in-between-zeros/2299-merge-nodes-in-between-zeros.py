# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nLst=[]
        cur=head
        cs=0
        while head:
            if head.val==0 and cs>0:
                nLst.append(cs)
                cs=0
            else:
                cs+=head.val
            head=head.next
         
        tail = head = ListNode(nLst[0])
        for x in nLst[1:]:
            tail.next = ListNode(x)  
            tail = tail.next
        return head
        