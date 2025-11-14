from ast import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=0):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = head

        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return new_head


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Normal list
    print("Test 1: [1, 2, 3, 4, 5]")
    list1 = build_linked_list([1, 2, 3, 4, 5])
    print("Original:", linked_list_to_list(list1))
    reversed1 = solution.reverseList(list1)
    print("Reversed:", linked_list_to_list(reversed1))
    
    # Test case 2: Single element
    print("\nTest 2: [42]")
    list2 = build_linked_list([42])
    print("Original:", linked_list_to_list(list2))
    reversed2 = solution.reverseList(list2)
    print("Reversed:", linked_list_to_list(reversed2))
    
    # Test case 3: Two elements
    print("\nTest 3: [1, 2]")
    list3 = build_linked_list([1, 2])
    print("Original:", linked_list_to_list(list3))
    reversed3 = solution.reverseList(list3)
    print("Reversed:", linked_list_to_list(reversed3))
    
    # Test case 4: Empty list
    print("\nTest 4: []")
    list4 = build_linked_list([])
    print("Original:", linked_list_to_list(list4))
    reversed4 = solution.reverseList(list4)
    print("Reversed:", linked_list_to_list(reversed4))