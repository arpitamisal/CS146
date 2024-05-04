Solutions:

1. Brute Force with nested for loops where time comp = O(n^2) and space comp = O(1)
2. HashMap where we store key value pairs, where we loop through the whole array but store the complement of each value and see if the hash map contains the complement. So, if we have an array [1, 4, 5, 6, 7] and our target is 11 then the hash map will store the values [10, 7, 6, 5, 4] so as soon as we find a complement which is of 4 which is 7, it will return the value. Time comp = O(n)
