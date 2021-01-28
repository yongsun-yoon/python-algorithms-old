# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        
        idx = 0
        while True:
            if l1:
                num1 += l1.val * 10 ** idx
                l1 = l1.next
                idx += 1
            else:
                break

        idx = 0
        while True:
            if l2:
                num2 += l2.val * 10 ** idx
                l2 = l2.next
                idx += 1
            else:
                break
        
        num = str(num1 + num2)
        node = None
        for n in num:
            node = ListNode(val=int(n), next=node)
        
        return node