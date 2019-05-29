from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        temp = deque()
        e = None
        while self.data:
            e = self.data.popleft()
            if self.data:
                temp.append(e)
            
        self.data = temp
            
        return e
            
        

    def top(self) -> int:
        """
        Get the top element.
        """
        
        temp = deque()
        e = None
        while self.data:
            e = self.data.popleft()
            temp.append(e)
        
        self.data = temp
            
        return e
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.data) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()