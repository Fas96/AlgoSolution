# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            if not node: return None
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        
        reversedL1 = reverse(l1)
        reversedL2 = reverse(l2)
        
        head = ListNode()
        carry = 0
        while reversedL1 or reversedL2 or carry:
            if reversedL1:
                carry += reversedL1.val
                reversedL1 = reversedL1.next
            if reversedL2:
                carry += reversedL2.val
                reversedL2 = reversedL2.next
            head.next = ListNode(carry % 10, head.next)
            carry //= 10
        return head.next
        