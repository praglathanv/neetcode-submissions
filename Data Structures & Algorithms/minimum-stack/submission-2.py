class MinStack:

    def __init__(self):
        self.arr = []  
        self.min_stack = []      

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.min_stack) != 0:
            val = min(val, self.min_stack[-1])

        self.min_stack.append(val)
        

    def pop(self) -> None:
        if len(self.arr) == 0:
            return
        
        self.min_stack.pop()
        return self.arr.pop()

    def top(self) -> int:
        if len(self.arr) == 0:
            return
        return self.arr[-1]

    def getMin(self) -> int:
        if len(self.arr) == 0:
            return
        
        return self.min_stack[-1]

        
