from math import remainder
from operator import truediv
from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def canReachLeaf(root:TreeNode):
    if not root:
        return False

    if not root.left and not root.right: #base case, for leaf node, if there is no right or left then it's a leaf node
        return True

    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True

    return False

def reachPath(root: TreeNode, path):
    if not root or root.val == 0:
        return False
        

    path.append(root.val)

    if not root.left and not root.right:
        return True
    
    if reachPath(root.left, path):
        #have to check this if it tracks in the right or not
        return True
    if reachPath(root.right, path):
        return True

    path.pop()

    return False

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #path = []

        if not root:
            return False

        targetSum = targetSum - root.val

        if not root.left and not root.right:
            return targetSum == 0 

        if self.hasPathSum(root.left, targetSum):
            return True

        if self.hasPathSum(root.right, targetSum):
            return True

        return False


if __name__ == "__main__":
    # Test case: root = [-15,10,20,null,null,15,5,-5], targetSum = 15
    # Tree structure:
    #      -15
    #     /    \
    #   10      20
    #         /    \
    #       15       5
    #              /
    #           -5
    root = TreeNode(-15)
    root.left = TreeNode(10)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(-5)
    
    solution = Solution()
    targetSum = 15
    
    print(f"Tree: root = [-15,10,20,null,null,15,5,-5]")
    print(f"TargetSum = {targetSum}")
    result = solution.hasPathSum(root, targetSum)
    print(f"Result: {result}")
    
    # Let's trace all paths to understand the result:
    # print("\nTracing all paths from root to leaf:")
    # print("Path 1: -15 -> 10 = -5")
    # print("Path 2: -15 -> 20 -> 15 = 20")
    # print("Path 3: -15 -> 20 -> 5 -> -5 = -15")
    # print(f"Does any path sum to {targetSum}? {result}")
    
    # # Test other target sums
    # print(f"\nTesting targetSum = 20: {solution.hasPathSum(root, 20)}")  # Should be True (path: -15+20+15)
    # print(f"Testing targetSum = -15: {solution.hasPathSum(root, -15)}")  # Should be True (path: -15+20+5+-5)
    # print(f"Testing targetSum = -5: {solution.hasPathSum(root, -5)}")  # Should be True (path: -15+10)
    # print(f"Testing targetSum = 0: {solution.hasPathSum(root, 0)}")  # Should be False