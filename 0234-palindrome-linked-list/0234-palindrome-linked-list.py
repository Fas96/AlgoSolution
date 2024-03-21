# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x=head
        arr=[]
        while x:
            arr.append(x.val)
            x=x.next
        arr=arr[::-1] 
        return  arr==arr[::-1] 