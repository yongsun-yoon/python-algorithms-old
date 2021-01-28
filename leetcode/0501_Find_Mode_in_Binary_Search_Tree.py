from collections import Counter
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def search(self, node):
        if node:
            self.nodes.append(node.val)
            self.search(node.left)
            self.search(node.right)
        
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.nodes = []
        self.search(root)
        cnt = Counter(self.nodes)
        max_cnt = max(cnt.values())
        ans = [k for k,v in cnt.items() if v == max_cnt]
        return ans