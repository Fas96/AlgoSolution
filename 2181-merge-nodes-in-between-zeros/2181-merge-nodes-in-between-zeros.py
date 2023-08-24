# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        tm=[]
        cur=head
        while  cur:
            tm.append(cur.val)
            cur=cur.next
        res=[]
        total=0
        
        for i in range(len(tm)):
            if tm[i]==0 and i!=0:
                res.append(total)
                total=0
            total+=tm[i]
        if not res: return None
        
        root=ListNode(res[0]) 
        cur=root 
        for val in res[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return root
        