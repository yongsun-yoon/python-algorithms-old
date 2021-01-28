"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def dfs(self, node):
        if not node.children:
            return 1
        else:
            return max([self.dfs(i) for i in node.children if i]) + 1
    
    def maxDepth(self, root: 'Node') -> int:
        if not root: 
            return 0
        else:
            return self.dfs(root)
        