from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=0, prev=0):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr =  self.head.next
        
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if index == 0 and curr and curr != self.tail:
            #we add to check if it's not tail because we have a dummy node there, so it returns -1 in that case
            return curr.val

        return -1

    def addAtHead(self, val: int) -> None:
        prev, next, node = self.head, self.head.next, ListNode(val)

        prev.next = node
        node.prev = prev
        next.prev = node
        node.next = next

    def addAtTail(self, val: int) -> None:
        prev, next, node = self.tail.prev, self.tail, ListNode(val)

        next.prev = node
        node.next = next
        prev.next = node
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index == 0:
            #it behaves as if we are adding at a tail
            prev, next, node =  curr.prev, curr, ListNode(val)

            prev.next = node
            node.prev = prev
            next.prev = node
            node.next = next

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if index == 0 and curr and curr != self.tail:
            #if we are at tail we don't need to delete as it's a dummy node
            prev, next = curr.prev, curr.next

            prev.next = next
            next.prev = prev


def dump_forward(linked_list: LinkedList) -> List[int]:
    values: List[int] = []
    node = linked_list.head.next
    while node and node != linked_list.tail:
        values.append(node.val)
        node = node.next
    return values


if __name__ == "__main__":
    dll = LinkedList()

    print("Initial:", dump_forward(dll))

    dll.addAtHead(10)
    dll.addAtHead(20)
    dll.addAtTail(5)
    print("After addAtHead/addAtTail:", dump_forward(dll))

    dll.addAtIndex(1, 15)
    dll.addAtIndex(0, 25)
    dll.addAtIndex(5, 0)  # attempt to add beyond current bounds
    print("After addAtIndex calls:", dump_forward(dll))

    print("get(0):", dll.get(0))
    print("get(2):", dll.get(2))
    print("get(10):", dll.get(10))

    dll.deleteAtIndex(1)
    dll.deleteAtIndex(0)
    dll.deleteAtIndex(10)  # delete out of range
    print("After deleteAtIndex calls:", dump_forward(dll))

