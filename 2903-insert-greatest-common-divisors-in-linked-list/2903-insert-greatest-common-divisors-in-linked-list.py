# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        l=[]
        h=head
        while h:
            l.append(h.val)
            h=h.next
        n=len(l)
        f=[l[0]]
        for i in range(n-1):
            f.append(math.gcd(l[i],l[i+1]))
            f.append(l[i+1])
       
        new_head = ListNode(f[0])
        current = new_head
        for value in f[1:]:
            current.next = ListNode(value)
            current = current.next
        
        return new_head 
        