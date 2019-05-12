class Element:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.cap = 10001
        self.data = [None] * self.cap
        
    def add(self, key: int) -> None:
        i = hash(key) % self.cap
        if not self.data[i]:
            self.data[i] = Element(key)
            self.size += 1
        else:
            ptr = self.data[i]
            while ptr:
                if ptr.key == key:
                    return
                elif ptr.next == None:
                    ptr.next = Element(key)
                    self.size += 1
                    return
                ptr = ptr.next

    def remove(self, key: int) -> None:
        i = hash(key) % self.cap
        if not self.data[i]:
            return
        else:
            ptr = prev = self.data[i]
            if ptr.key == key:
                self.data[i] = prev.next
                self.size -= 1
                return
            ptr = ptr.next
            while ptr:
                if ptr.key == key:
                    prev.next = ptr.next
                    self.size -= 1
                    return
                prev, ptr = prev.next, ptr.next
                    

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = hash(key) % self.cap
        if not self.data[i]:
            return False
        else:
            ptr = self.data[i]
            while ptr:
                if ptr.key == key:
                    return True
                ptr = ptr.next
            return False
            
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)