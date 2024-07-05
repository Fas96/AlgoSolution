# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ls=[]
        if not head or not head.next:
            return [0,0]
        while head:
            ls+=[head.val]
            head=head.next
        mnL,mxL=[],[]
        n=len(ls)
        if n < 3: return [-1,-1]
        def findLocalMnMx(arr,n):
            lmx ,lmn= None,None
            idxmx,idxmn=-float('inf'),float('inf')
            
            for i in range(1, n - 1):
                if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]) or (arr[i] < arr[i - 1] and arr[i] < arr[i + 1]):
                    if lmx is None:
                        lmn=lmx=i
                    else:
                        idxmn=min(idxmn,i-lmx)
                        idxmx=max(idxmx,i-lmn)
                        lmx=i
            if (idxmn==float('inf') or idxmx==-float('inf')):return [-1,-1]
            print(idxmn,idxmx)
            return [idxmn,idxmx]
        
        return findLocalMnMx(ls,n)

        