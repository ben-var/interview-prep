class Node:
    def __init__(self, key, value):
        self.item = (key, value)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.capacity = 3000
        self.data = [None] * self.capacity
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = hash(key) % self.capacity
        if self.data[index] == None:
            self.data[index] = Node(key, value)
            self.size += 1
        else:
            pointer = self.data[index]
            while pointer:
                if pointer.item[0] == key:
                    pointer.item = (key, value)
                    return
                if not pointer.next: break
                pointer = pointer.next  
            pointer.next = Node(key, value)
            self.size += 1

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = hash(key) % self.capacity        
        pointer = self.data[index]
        while pointer:
            if pointer.item[0] == key:
                return pointer.item[1]
            pointer = pointer.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = hash(key) % self.capacity
        if self.data[index] == None:
            return
        
        pointer = prev = self.data[index]
        if pointer.item[0] == key:
            self.data[index] = pointer.next
            self.size -= 1
        else:
            pointer = pointer.next
            while pointer:
                if pointer.item[0] == key:
                    prev.next = pointer.next
                    self.size -= 1
                    return
                prev = pointer
                pointer = pointer.next
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)