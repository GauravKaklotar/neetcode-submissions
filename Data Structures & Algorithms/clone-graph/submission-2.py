"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # ------------------- Solution 1 ------------------
        # import copy
        # return copy.deepcopy(node)

        # ------------------- Solution 2 ------------------
        if not node:
            return None
        
        clones = {}

        def solve(node):
            
            if node in clones:
                return clones[node]

            copy = Node(node.val)
            clones[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(solve(nei))
            
            return copy

        return solve(node)


