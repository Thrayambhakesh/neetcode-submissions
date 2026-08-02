class MinStack:
    
    def __init__(self):
        self.L=[]

    def push(self, val: int) -> None:
        self.L.append(val)

    def pop(self) -> None:
        a=self.L.pop()

    def top(self) -> int:
        return self.L[-1]

    def getMin(self) -> int:
        return min(self.L)
