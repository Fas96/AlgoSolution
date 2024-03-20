# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = list1
        prev = dummy 
        for _ in range(a):
            prev = prev.next 
        curr = prev
        for _ in range(b - a + 2):   
            curr = curr.next
         
        prev.next = list2
         
        while prev.next:
            prev = prev.next
        
        
        prev.next = curr 
        return dummy.next
        
            