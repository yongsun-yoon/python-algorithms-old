# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = []
        node = head
        while node:
            num.append(node.val)
            node = node.next
        
        num = ''.join(map(str, num))
        return int(num, 2)
