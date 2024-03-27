We can invert a binary search tree by swaping the left and right children of each node in the tree. To solve this problem, I followed this logic:
If the current node is null, then return null since there is nothing to invert.
Swap the left and right children of the current node.
Recursively call the invert function on both children (which are now swapped).
Continue this process until every node has been visited and had its children swapped.
Return the original root, which now points to an inverted tree structure.
