
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Val = []
        l2Val = []
        def listNodeToVal(l: Optional[ListNode], val: list):
            while l:
                val.append(l.val)
                l = l.next
                
        listNodeToVal(l1, l1Val)
        listNodeToVal(l2, l2Val)
        # reverse
        
        l1Val.reverse()
        l2Val.reverse()
        
        l1Val = int(''.join(map(str, l1Val)))
        l2Val = int(''.join(map(str, l2Val)))
        
        ans = l1Val + l2Val
        
        ans = list(map(int, str(ans)))
        ans.reverse()
        
        dummy = ListNode()
        cur = dummy
        for node in ans:
            cur.next = ListNode(node)
            cur = cur.next
        return dummy.next
        