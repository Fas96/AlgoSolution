# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return None
        dq = deque()
        cur = head
        while cur:
            dq.append(cur)
            cur = cur.next
        dq.popleft() 
        cur = head
        while dq:
            cur.next = dq.pop()
            cur = cur.next
            if dq:
                cur.next = dq.popleft()
                cur = cur.next

        cur.next = None