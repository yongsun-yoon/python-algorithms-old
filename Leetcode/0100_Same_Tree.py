# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node, arr):
        if not node:
            arr.append('null')
        else:
            arr.append(node.val)
            self.dfs(node.left, arr)
            self.dfs(node.right, arr)
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_arr, q_arr = [], []
        self.dfs(p, p_arr)
        self.dfs(q, q_arr)
        ans = all([i == j for i,j in zip(p_arr, q_arr)])
        return ans