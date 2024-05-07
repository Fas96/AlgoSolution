import sys
sys.set_int_max_str_digits(0)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(str(head.val))
            head=head.next
        num=int("".join(arr))*2
        du=ListNode(-1)
        cur=du
        for x in [int(d) for d in str(num)]:
            cur.next=ListNode(x)
            cur=cur.next
        return du.next