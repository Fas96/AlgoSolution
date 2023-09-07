# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes= []
        while head:
            nodes.append(head.val)
            head = head.next
        delAt=len(nodes)-n
        nodes=nodes[:delAt]+nodes[delAt+1:]
        dummy = ListNode()
        cur = dummy
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return dummy.next
        