# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans = None

        def inorder(node):
            nonlocal k, ans
            if not node:
                return
            
            inorder(node.left)
            k -= 1
            if k == 0:
                ans = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return ans



        # ************** Brute force --> inorder - list - kth ***********
        # l = []

        # def inorder(node):
        #     nonlocal l

        #     if not node:
        #         return
            
        #     inorder(node.left)
        #     l.append(node.val)
        #     inorder(node.right)
        
        # inorder(root)
        # return l[k-1]