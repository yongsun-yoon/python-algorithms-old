# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recur(self, node):
        if node:
            l, r = node.left, node.right
            base = str(node.val)
            if l and r:
                sub = f'({self.recur(l)})({self.recur(r)})'
            elif l:
                sub = f'({self.recur(l)})'
            elif r:
                sub = f'()({self.recur(r)})'
            else:
                sub = ''
            return base + sub
        else:
            return ''
        
    def tree2str(self, t: TreeNode) -> str:
        ans = self.recur(t)
        return ans