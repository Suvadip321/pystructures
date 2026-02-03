class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def search(root, val):
    curr = root
    while curr:
        if curr.data == val:
            return True
        elif val < curr.data:
            curr = curr.left
        else:
            curr = curr.right
    return False

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.data:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def delete(root, val):
    """
    case 1: deletion of leaf node (0 child)
    case 2: deletion of node having 1 child
    case 3: deletion of node having 2 children (we have to find inorder successor of that node)
    """
    if root is None:
        return None
    if val < root.data:
        root.left = delete(root.left, val)
    elif val > root.data:
        root.right = delete(root.right, val)
    else:
        # case 1 & 2
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # case 3
        # find inorder successor
        curr = root.right
        while curr.left:
            curr = curr.left
        root.data = curr.data
        root.right = delete(root.right, curr.data)
    return root
