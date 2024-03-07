# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        keepNode=[]
        dummy=head
        while dummy:
            keepNode.append(dummy)
            dummy=dummy.next
        N=len(keepNode)
        fm=N//2
        d=head
        while fm:
            fm-=1
            d=d.next 
        return d
        