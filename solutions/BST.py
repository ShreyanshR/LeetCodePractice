class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root: TreeNode, val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        return insert(root.right, val)
    elif val < root.val:
        return insert(root.left, val)

    return root

def minNode(root: TreeNode):
    curr = root

    while curr and curr.left:
        curr = curr.left
    
    return curr

def remove(root: TreeNode, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min = minNode(root.right)
            root.val = min.val
            root.right = remove(root.right, min.val)
    
    return root

