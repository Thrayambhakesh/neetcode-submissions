# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calc(root):
            if not root:
                return (True,0)
            if root.left==None and root.right==None:
                return (True,1)
            left=calc(root.left)
            a,b=left
            right=calc(root.right)
            c,d=right

            if not a or not c:
                return (False,0)
            if abs(b-d)>1:
                return (False,0)
            return (True,1+max(b,d))
        b,_=calc(root)
        return b
            