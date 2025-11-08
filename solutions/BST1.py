class TreeNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.right = None
        self.left = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)

        if self.root == None:
            self.root = newNode
            return

        current = self.root

        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return 
                current = current.left

            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            
            else:
                #if the value is the same, replace inplace
                current.val = val

    def get(self, key: int)-> int:
        curr = self.root

        while curr != None:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val #this is when it found the exact key

        return -1 #in the case when value is none

    def getMin(self) -> int:
        current = self.findMind(self.root)
        return current.val if current else -1

    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        current = self.root
        while current and current.right: 
            current = current.right

        return current.val if current else -1

    def remove(self, key:int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self,curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None
        
        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)

        elif key < curr.left:
            curr.left = self.removeHelper(curr.left, key)

        else:
            if curr.right == None:
                return curr.left
            elif curr.right == None:
                return curr.right

            else:
                minNode = self.findMin()

            minNode = self.findMin()




