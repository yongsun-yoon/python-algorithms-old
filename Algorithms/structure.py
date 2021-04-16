
class FixedStack(object):
    def __init__(self, maxlen):
        self.data = [None for _ in range(maxlen)]
        self.maxlen = maxlen
        self.pointer = 0
    
    def __len__(self):
        return self.pointer
    
    def is_empty(self):
        return self.pointer == 0
    
    def is_full(self):
        return self.pointer == self.maxlen
    
    def clear(self):
        self.pointer = 0

    def push(self, val):
        if self.is_full(): return 'Stack is full'
        self.data[self.pointer] = val
        self.pointer += 1
    
    def pop(self):
        if self.is_empty(): return 'Stack is empty'
        self.pointer -= 1
        return self.data[self.pointer]


class Stack(object):
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self) == 0
    
    def clear(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()


class FixedQueue(object):
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.data = [None for _ in range(maxlen)]
        self.front = 0
        self.rear = 0
        self.num_data = 0
    
    def __len__(self):
        return self.num_data
    
    def is_empty(self):
        return self.num_data == 0
    
    def is_full(self):
        return self.num_data == self.maxlen
    
    def enque(self, val):
        if self.is_full(): return "Queue is full"
        self.data[self.rear] = val
        self.rear += 1
        self.num_data += 1
        if self.rear == self.maxlen:
            self.rear = 0
    
    def deque(self):
        if self.is_empty(): return "Queue is empty"
        val = self.data[self.front]
        self.front += 1
        self.num_data -= 1
        if self.front == self.maxlen:
            self.front = 0
        return val


