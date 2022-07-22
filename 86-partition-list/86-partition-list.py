# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        emptyNode = ListNode()
        emptyNode.next = head
        lcheck = emptyNode
        llt = emptyNode
        
        check = lcheck.next
        while check is not None:
            if check.val < x: 
                lcheck.next = check.next
                check.next = None
                
              
                tmp = llt.next
                llt.next = check
                check.next = tmp
                
               
                llt = llt.next
            
            lcheck, check = check, check.next
        
        return emptyNode.next