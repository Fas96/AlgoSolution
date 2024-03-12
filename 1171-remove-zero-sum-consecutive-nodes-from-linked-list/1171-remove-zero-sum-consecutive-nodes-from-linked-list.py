# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefixSum = 0
        sumTable = {0: dummy} 
        while head:
            prefixSum += head.val
            sumTable[prefixSum] = head
            head = head.next

         
        head = dummy
        prefixSum = 0
 
        while head:
            prefixSum += head.val 
            head.next = sumTable[prefixSum].next
            head = head.next

        return dummy.next
        
        