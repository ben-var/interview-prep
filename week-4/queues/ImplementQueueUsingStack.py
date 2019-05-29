class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        temp = []
        while self.data:
            x = self.data.pop()
            if self.data:
                temp.append(x)
        while temp:
            self.data.append(temp.pop())
        
        return x

    
    def peek(self) -> int:
        """
        Get the front element.
        """
        temp = []
        while self.data:
            x = self.data.pop()
            temp.append(x)
        while temp:
            self.data.append(temp.pop())
        
        return x
        
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.data) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()