class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def preorder(root):
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.data)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res


def inorder(root):
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.data)
        dfs(node.right)
    dfs(root)
    return res


def postorder(root):
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.data)
    dfs(root)
    return res

