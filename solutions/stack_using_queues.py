from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, val: int):
        self.q2.append(val)

        while self.q1:
            self.q2.append(self.q1.popleft())
        
        #swapping of queues, it resets the queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


if __name__ == "__main__":
    stack = MyStack()
    
    print("Initial empty check:", stack.empty())
    
    # Test push operations
    print("\nPushing 1, 2, 3...")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack empty?", stack.empty())
    print("Top element:", stack.top())
    
    # Test pop operations
    print("\nPopping elements (should be 3, 2, 1):")
    print("Pop:", stack.pop())
    print("Top after first pop:", stack.top())
    print("Pop:", stack.pop())
    print("Top after second pop:", stack.top())
    print("Pop:", stack.pop())
    print("Stack empty after all pops?", stack.empty())
    
    # Test more operations
    print("\nPushing 10, 20, 30...")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top:", stack.top())
    print("Pop:", stack.pop())
    print("Top:", stack.top())
    print("Pop:", stack.pop())
    print("Top:", stack.top())
    print("Pop:", stack.pop())
    print("Final empty check:", stack.empty())