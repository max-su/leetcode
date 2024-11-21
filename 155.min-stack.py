class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        curr_min = val if not self.stack else min(self.getMin(), val)
        self.stack.append((val, curr_min))
        

    def pop(self) -> None:
        if not self.stack:
            raise IndexError()
        self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            raise IndexError()
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError()
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()