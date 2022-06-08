# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
 
        ptr1,ptr2=headA,headB
        
        while ptr1!=ptr2:
            if ptr1 is None:
                ptr1=headB
            else:
                ptr1=ptr1.next
            if ptr2 is None:
                ptr2=headA
            else:
                ptr2=ptr2.next
        return ptr1
                
            
        
        