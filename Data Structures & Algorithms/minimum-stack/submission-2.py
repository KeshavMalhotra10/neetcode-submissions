class MinStack:

    def __init__(self):
        self.st = []
        

    def push(self, val: int) -> None:
        self.st.append(val)
        

    def pop(self) -> None:
        self.st.pop()

        
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        minValue = self.st[-1]
        for element in self.st:
            if element < minValue:
                minValue = element
        return minValue

        
