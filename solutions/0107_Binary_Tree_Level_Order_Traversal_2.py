from typing import List
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result, heap = {}, [(0, 0, root)]

        while heap:
            level, pos, tree = heapq.heappop(heap)
            result.setdefault(level, [])
            result[level].append(tree.val)
            
            if tree.left:
                heapq.heappush(heap, (level-1, pos, tree.left))
            if tree.right:
                heapq.heappush(heap, (level-1, pos+1, tree.right))
        
        result = sorted(result.items(), key=lambda x : x[0])
        result = [list(i[1]) for i in result]
        return result