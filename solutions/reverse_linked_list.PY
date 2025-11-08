 #Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:

            nxt = curr.next
            print(f'nxt: {nxt}')
            #this line is confusing but it points to the prev pointer
            #for ex 1, 2, 3
            #when the curr pointer is at 2, this will point prev to 1, the when below we do prev = curr, it will set prev = 2
            #when the curr pointer is at 3, and curr.next = null
            #this creates a conundrum, but then in then we do curr.next = prev = 2
            curr.next = prev
            print(f'curr.next, prev: {curr.next, prev}')
            prev = curr
            print(f'prev: {prev}')
            curr = nxt
            print(f'curr: {curr}')

        return prev


if __name__ == "__main__":
    # Create ListNode objects instead of a list
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)

    s = Solution()
    result = s.reverseList(head)
    
    # Print the reversed list
    curr = result
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")