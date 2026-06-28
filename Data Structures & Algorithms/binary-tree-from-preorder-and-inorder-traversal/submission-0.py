# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        index = {value : i for i, value in enumerate(inorder)}
        pre_ind = 0

        def dfs(left, right):
            nonlocal pre_ind
            if left > right:
                return None
            
            root_val = preorder[pre_ind]
            pre_ind += 1

            root = TreeNode(root_val)

            mid = index[root_val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root
        
        return dfs(0, len(inorder) - 1)