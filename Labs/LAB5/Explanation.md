We can determine if a binary tree is a valid binary search tree by looking at a BSTs properties. To solve this problem, I followed this logic:
Begin with the root node.
At each node, compare its value to ensure it fits within the current range.
When moving to the left child, update the upper bound of the range to be the current node's value, since the left child must be less than its parent.
When moving to the right child, update the lower bound of the range to be the current node's value, since the right child must be greater than its parent.
If at any point a node does not satisfy the range requirements, return false.
If all nodes satisfy the requirements, then the tree is a valid BST.
