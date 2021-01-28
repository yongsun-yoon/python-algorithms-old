# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        
        nums = [head.val]
        prev = head
        
        while prev.next:
            node = prev.next
            
            if node.val in nums:
                prev.next = node.next
            else:
                nums.append(node.val)
                prev = node        
            
        return head