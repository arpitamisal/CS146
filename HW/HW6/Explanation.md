Solutions:

1. Brute Force: Find a pair then add the third element one by one until you find an answer, if you don’t then move to the next number for the 2nd element and then do the same. Time Comp: O(n^3)
2. Hashset: If our array has less than 3 elements, return empty list, then first sort your array, then create a hashset, results, then have a for loop from 0 to length -2 and create 2 pointers, left = i+1 and right = length - 1, then have a while loop until left is less than right, then have a value sum where arr[i] + arr[left] + arr[right], and if the sum == 0 then add the result into the hashset, then increment left and right, and if the sum is less than 0 then increment only left, else increment only right, then at the end return new ArrayList<>(result), TIME COMP= O(n^2)
