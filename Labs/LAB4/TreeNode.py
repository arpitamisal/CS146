from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Approach
def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root


# Iterative Approach
def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return None

    queue = deque([root])
    while queue:
        current = queue.popleft()
        current.left, current.right = current.right, current.left
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return root
