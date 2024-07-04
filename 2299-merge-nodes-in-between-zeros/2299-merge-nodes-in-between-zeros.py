# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nLst=[]
        cur=head
        while head:
            nLst.append(head.val)
            head=head.next
        cLst=[]
        cs=0
        for v in nLst:
            if v==0 and cs>0:
                cLst.append(cs)
                cs=0
            else:
                cs+=v
        tail = head = ListNode(cLst[0])
        for x in cLst[1:]:
            tail.next = ListNode(x)  
            tail = tail.next
        return head
        