class Node:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.d = {}
        self.cap = capacity
        self.head, self.tail = Node(), Node()
      
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self._remove(self.d[key])
        self._insert(self.d[key])
        return self.d[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self._remove(self.d[key])
        node = Node(key, value)
        self._insert(node)
        self.d[key] = node
            
        if len(self.d) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            self.d.pop(lru.key)