# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        sz = 0 
        while cur:
            sz += 1
            cur = cur.next

        each = sz // k
        remainder = sz % k

        result = []
        cur = head

        for i in range(k):
            sublist_size = each + 1 if i < remainder else each

            if sublist_size == 0:
                result.append(None)
            else:
                result.append(cur)

                for j in range(sublist_size - 1):
                    cur = cur.next

                next_node = cur.next
                cur.next = None
                cur = next_node

        return result
            
        