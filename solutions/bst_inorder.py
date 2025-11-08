from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        if not root:
            return
        
        self.inorderTraversal(root.left)
        inorder.append(root.val)
        self.inorderTraversal(root.right)
        inorder.append(root.val)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(node):
            if not node:
                return
                
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        print(res)

        return res[k-1]

    def buildBST(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #pre ordeer -> [3, 9, 20, 15, 7]
        #in order [9, 3, 15, 20, 7]

        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index + 1:]

        preorder_left = preorder[1:1+root_index]
        preorder_right = preorder[1+root_index:]

        root.left = self.buildBST(preorder_left, inorder_left)
        root.right = self.buildBST(preorder_right, inorder_right)

if __name__ == "__main__":
    root = [1,2,3,None,4,5,None]

    s = Solution()
    s.kthSmallest(root, 3)
    