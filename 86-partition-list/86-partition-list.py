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
        last_check = emptyNode
        last_less_than = emptyNode
        
        check = last_check.next
        while check is not None:
            if check.val < x:
                # remove check
                last_check.next = check.next
                check.next = None
                
                # add check after the last_less_than
                tmp = last_less_than.next
                last_less_than.next = check
                check.next = tmp
                
                # update pointers
                last_less_than = last_less_than.next
            
            last_check, check = check, check.next
        
        return emptyNode.next