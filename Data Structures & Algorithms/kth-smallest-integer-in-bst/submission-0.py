# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Brute force --> inorder - list - kth
        l = []

        def inorder(node):
            nonlocal l

            if not node:
                return
            
            inorder(node.left)
            l.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return l[k-1]