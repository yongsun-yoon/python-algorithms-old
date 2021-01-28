from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = {}
        queue = [(root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            if node:
                ans.setdefault(level, [])
                ans[level].append(node.val)
                
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
                
        return [sum(v)/len(v) for v in ans.values()]