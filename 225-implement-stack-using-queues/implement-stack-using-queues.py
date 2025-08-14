class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        if not self.q1: return -1
        for _ in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        for i in range(len(self.q2)):
            self.q1.append(self.q2.popleft())
        return val
        

    def top(self) -> int:
        if not self.q1: return -1
        for _ in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        for _ in range(len(self.q2)):
            self.q1.append(self.q2.popleft())
        self.q1.append(val)
        return val
        

    def empty(self) -> bool:
        return not bool(self.q1)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()