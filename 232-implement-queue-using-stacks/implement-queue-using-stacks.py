class MyQueue:

    def __init__(self):
        self.stack = []
        self.size = 0
        

    def push(self, x: int) -> None:
        stack2 = []
        while self.stack:
            stack2.append(self.stack.pop())
        self.stack.append(x)
        while stack2:
            self.stack.append(stack2.pop())
        self.size += 1

    def pop(self) -> int:
        if self.size <= 0: return -1
        self.size -= 1
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]
        

    def empty(self) -> bool:
        return not bool(self.stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()