# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        
        while True:
            if hasattr(head, 'visited'):
                return True
            else:
                head.visited = True
                if head.next:
                    head = head.next
                else:
                    return False
            