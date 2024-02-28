# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.l1=[]
        def trace(l):
            if not l: return self.l1
            self.l1.append(l.val)
            trace(l.next)
        trace(list1)
        trace(list2)
        v=sorted(self.l1)
        dummy = ListNode(0)
        current = dummy
        for val in v:
            current.next = ListNode(val)
            current = current.next   
        
        return dummy.next
        
        