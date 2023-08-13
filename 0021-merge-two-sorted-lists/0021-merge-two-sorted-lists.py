# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        minH1 = []
        minH2 = []
        cur1 = list1
        cur2 = list2
        while cur1:
            heapq.heappush(minH1, cur1.val)
            cur1 = cur1.next
        while cur2:
            heapq.heappush(minH2, cur2.val)
            cur2 = cur2.next
        dummy = ListNode()
        cur = dummy
        while minH1 and minH2:
            if minH1[0] < minH2[0]:
                cur.next = ListNode(heapq.heappop(minH1))
            else:
                cur.next = ListNode(heapq.heappop(minH2))
            cur = cur.next
        while minH1:
            cur.next = ListNode(heapq.heappop(minH1))
            cur = cur.next
        while minH2:
            cur.next = ListNode(heapq.heappop(minH2))
            cur = cur.next
        return dummy.next