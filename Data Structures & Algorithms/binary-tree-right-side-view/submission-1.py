# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque([root])
        L=[]
        if not root:
            return []
        while q:

            size=len(q)
            level=[]

            for i in range(size):
                node=q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            L.append(level)

        L2=[]
        for i in L:
            L2.append(i[-1])
        return L2

        