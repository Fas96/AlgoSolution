class Solution(object):
    def reverseBetween(self, head, m, n):
        hat = ListNode(0)
        hat.next, start = head, hat

        for i in range(m):
            beforeStart, start = start, start.next

        for i in range(n - m):
            beforeStart.next, start.next, beforeStart.next.next = start.next, start.next.next, beforeStart.next

        return hat.next