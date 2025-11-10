from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next

            node = node.next
        
        #null case in case of one of them is empty
        node.next = list1 or list2

        return dummy

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_python_list(head: Optional[ListNode]) -> List[int]:
    values: List[int] = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


if __name__ == "__main__":
    list1_values = [1, 2, 4]
    list2_values = [1, 3, 5]

    list1 = build_linked_list(list1_values)
    list2 = build_linked_list(list2_values)

    solution = Solution()
    merged_head = solution.mergeTwoList(list1, list2)

    print("Input list1:", list1_values)
    print("Input list2:", list2_values)
    print("Merged output:", linked_list_to_python_list(merged_head))