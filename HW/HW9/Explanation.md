We can find the lowest common ancestor in a binary search tree by using its inherent properties. To solve this problem, I followed this logic:
Start with the root of the BST.
If both p and q are greater than the root, then move to the right child of the root.
If both p and q are less than the root, then move to the left child of the root.
If one of p or q is less and the other is greater than the root (or one of them is equal to the root), then the root is the LCA.
