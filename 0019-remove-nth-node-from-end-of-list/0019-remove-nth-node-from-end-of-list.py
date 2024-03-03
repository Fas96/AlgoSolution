# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d=head
        lis=[]
        while d:
            if not d: return
            lis.append(d)
            d=d.next
         
        held=[]
        
        N = len(lis)
        skip_index = N - n
 
        if skip_index == 0:
            return head.next 
        lis[skip_index - 1].next = lis[skip_index].next if skip_index + 1 < N else None

        return head
        
            
        