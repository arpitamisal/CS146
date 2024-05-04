Solutions:

1. Brute Force: Where you go linearly where, you go one by one from the beginning of the array and check if version is good or bad. O(n).
2. Binary Search: Time Comp = O(log n), where we will have 2 pointers left = 0 and right = n, and while left is not less than right we will have a midpoint of left + (right - left) / 2, where if the bad version is the midpoint then the midpoint become right, else the midpoint become the left. Then if the left == right and the bad version is left then we return left. or else we return -1 where there is no bad version.
