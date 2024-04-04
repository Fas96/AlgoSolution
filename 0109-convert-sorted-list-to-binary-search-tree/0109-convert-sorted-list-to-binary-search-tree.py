# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        def createBST(nms,start,end):
            if start<=end:
                mid=(start+end)//2
                node=TreeNode(nms[mid])
                node.left=createBST(nms,start,mid-1)
                node.right=createBST(nms,mid+1,end)
                return node
        return createBST(nums,0,len(nums)-1)
        