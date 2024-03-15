# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=head
        arr=[]
        while x:
            arr.append(x.val)
            x=x.next
        arr=arr[::-1]
        xx=ListNode(0)
        cu=xx
        
        for x in arr:
            cu.next=ListNode(x)
            cu=cu.next
        return xx.next
        