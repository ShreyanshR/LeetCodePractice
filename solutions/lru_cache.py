class Node:
    def __init__(self, key, val):
        self.key = key
        self.prev = None
        self.next = None
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node) #removing from the Linked List
        self._add_to_tail(node) # adding it to the tail for recently used
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node) #if we access it, it becomes LRU
            self._add_to_tail(node)

        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key] #deleting the node

            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_tail(new_node)

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = node.next
        next_node.prev = node.prev

    def _add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node