# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [(root, 0, None)] # node, depth, parent
        x_info, y_info = (-1, -1, False), (-1, -1, False) # depth, parent, done
        
        while queue and not (x_info[2] and y_info[2]):
            node, depth, parent = queue.pop(0)
            if node:
                if node.val == x:
                    x_info = (depth, parent, True)
                elif node.val == y:
                    y_info = (depth, parent, True)
                
                queue.append((node.left, depth+1, node.val))
                queue.append((node.right, depth+1, node.val))
        

        return x_info[0] == y_info[0] and x_info[1] != y_info[1]