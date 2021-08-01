# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recur_fn(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.recur_fn(node.left)
            self.recur_fn(node.right)
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.recur_fn(root)
        return root