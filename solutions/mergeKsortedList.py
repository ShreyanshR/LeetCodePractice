from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next = None):
        self.next = next
        self.val = val

class Solution:
    def mergeKlists(self, lists: List[ListNode]) -> ListNode:
        #Edge Cases if list is empty
        if not lists or len(lists) == 0:
            return 

        """
        we will merge basically two sorted list pair by pair, and we have done the pair soln as an easy problem
        """

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None 
                
                #print(l1,l2)# We are checking this to just see if there is only 1 list, and we do by checking if i+1 list exist

                mergedLists.append(self.mergeList(l1,l2))

            lists = mergedLists

        return lists


    
    def mergeList(self, l1, l2):
        dummy = head = ListNode()
        
        while l1 and l2:
            print(l1.val, l2.val)
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            print(head.val)
            head = head.next

        #if one of the list finishes early then we will merge the rest of the list
        head.next = l1 or l2

        print(dummy)

        return dummy.next


def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Helper function to convert a list to a ListNode."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper function to convert a ListNode to a list for printing."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    solution = Solution()
    
    # Test case
    lists = [[1, 2, 4], [1, 3, 5], [3, 6]]
    
    # Convert lists to ListNode objects
    list_nodes = [list_to_linked_list(lst) for lst in lists]
    
    # Merge the lists
    result = solution.mergeKlists(list_nodes)
    
    # Convert result back to list and print
    if result:
        merged_list = linked_list_to_list(result[0] if isinstance(result, list) else result)
        print(f"Input lists: {lists}")
        print(f"Merged result: {merged_list}")
    else:
        print("Result is None")
