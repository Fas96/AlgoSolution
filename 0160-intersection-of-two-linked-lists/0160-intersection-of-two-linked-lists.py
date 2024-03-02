# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sA,Na,sB,Nb=headA,0,headB,0
        while sA:
            sA=sA.next
            Na += 1
        while sB:
            sB=sB.next
            Nb += 1
            
         
        def go(head,noMove):
            while noMove>0:
                head=head.next
                noMove-=1
            return head
        if sA != sB:
            return None
        if Na>Nb:
            headA=go(headA,Na-Nb)
        elif Nb> Na:
            headB=go(headB,Nb-Na)
        
        while headA != headB:
            headA=headA.next
            headB=headB.next
            
        return headB
        