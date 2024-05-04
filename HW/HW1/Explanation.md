Solutions

1. Brute Force: First we make a new string, remove all the chars other than alphanumeric chars and make it lowercase. Then, have a for loop to reverse the string and then compare the 2 strings one by one to see if they match.
2. Two Pointer: First we make a new string, remove all the chars other than alphanumeric chars and make it lowercase. Then we will have 2 pointers, one at the beginning of the string and one at the end of the string, and while our pointer a is not less than or equal to pointer b, we will check if the character at pointer a is not equal to pointer a and return false, but if it is equal, we will increment pointer a and decrement pointer b and then outside the while loop it will return true. TIME COMP: O(n)
