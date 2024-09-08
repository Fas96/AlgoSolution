# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        sizer=head
        idx=0
        while sizer:
            idx+=1
            sizer=sizer.next
        part_size, extra_nodes = divmod(idx, k)

        current = head
        result = []
        for i in range(k):
            part_head = current
            for j in range(part_size - 1 + (i < extra_nodes)):
                if current:
                    current = current.next
            if current:
                next_node = current.next
                current.next = None
                current = next_node
            result.append(part_head)
        
        return result