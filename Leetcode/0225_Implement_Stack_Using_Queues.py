from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        len_q = len(self.q)
        sub_q = deque([])
        while len(sub_q) < len_q - 1:
            val = self.q.popleft()
            sub_q.append(val)
            
        ret = self.q.popleft()
        self.q = sub_q
        return ret
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()