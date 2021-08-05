from random import randint


class Stack:
    """Last In First Out
    """

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()  # IndexError if stack empty

    def top(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() < 1

    def __str__(self):
        return f"Stack: {self.stack}"


class Queue:
    """First In First Out
    Alternative: 
        from collections import deque
        append() and popleft()
    """

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() < 1

    def __str__(self):
        return f"Queue: {self.queue}"


if __name__ == "__main__":
    s = Stack()
    print(s)
    for i in range(4):
        s.push(i)
    print(s)
    print(s.pop())
    print(s.size())
    print(s.is_empty())

    q = Queue()
    for _ in range(5):
        q.enqueue(randint(2, 100))
    print(q)
    print(q.dequeue())
    print(q.size())
