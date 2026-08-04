# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        def calc(root):
            if root==None:
                return 0
            if root.left==None and root.right==None:
                return 1

            left=calc(root.left)
            right=calc(root.right)
            self.maxi=max(self.maxi,left+right)
            return 1+max(left,right)

        calc(root)
        return self.maxi


        
            
            