from collections import deque
from turtle import right
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def bfs(self, root: TreeNode):
        queue = deque()

        if root:
            queue.append(root)

        level = 0

        curr = []
        res = []

        while len(queue) > 0:
            print("level: ", level)

            for i in range(len(queue)):
                curr = queue.popleft()
                res.append(curr)
                print("res: ", res) #will pop the element by left
                print("queue lenght, after popping: ", len(queue))

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                print("queue: ", queue)

                print("queue lenght: ", len(queue))

                #the loop will end here bcoz imagine we did for the root, if the root is popped then there
                # is nothing in the queue so len is not greter than 0

            level += 1

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        queue = deque([root])

        level = len(queue)

        while len(queue) > 0:
            curr = queue.popleft()
            res.append(curr.val)

            if curr.right:
                queue.append(curr.right)

            level += 1

        return res



if __name__ == "__main__":
    S = Solution()
    
    # Create a sample binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Testing rightSideView:")
    print("Right side view:", S.rightSideView(root))
    
    print("\n" + "="*50)
    print("Testing rightSideView with empty tree:")
    print("Right side view:", S.rightSideView(None))
    
    print("\n" + "="*50)
    print("Testing rightSideView with single node:")
    single_node = TreeNode(10)
    print("Right side view:", S.rightSideView(single_node))
    
    print("\n" + "="*50)
    print("Testing rightSideView with different tree structure:")
    # Create a tree:    1
    #                 /   \
    #                2     3
    #               /     / \
    #              4     5   6
    #             /
    #            7
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(6)
    root2.left.left.left = TreeNode(7)
    
    print("Right side view:", S.rightSideView(root2))