Problem 1:

    Best Case: The best case occurs when the input array is already sorted. In each iteration of the main loop, the current element is already greater than or equal to the elements in the sorted array, which means the inner loop (the while loop) does not execute. Therefore, the algorithm makes n-1 comparisons and 0 shifts, resulting in a best-case time complexity of O(n).

    Average Case: On average, half of the inner loop comparisons need to be made for each pass through the array. This results in approximately 1/2 * n * (n - 1) comparisons, simplifying to O(n^2).

    Worst Case: The worst case occurs when the array is sorted in reverse order. Every insertion requires shifting all the elements sorted so far. The first element requires 0 shifts, the second requires 1 shift, the third requires 2 shifts, and so on, up to n-1 shifts for the last element. This results in 1 + 2 + ... + (n - 1) comparisons and shifts, which simplifies to O(n^2).

Problem 2:

for each row in A

    for each column in B

        for each element in the row of A and column of B


    Best Case: The time complexity of matrix multiplication does not vary based on the content of the matrices. The number of operations required is always determined by the dimensions of the input matrices. Thus, the best case time complexity is O(n^3) for square matrices of size n x n or generally O(rows_A * cols_B * cols_A).

    Average Case: Similarly to the best case, the average case remains the same because the algorithm's behavior does not change with different data distributions within the matrices. It is also O(rows_A * cols_B * cols_A).

    Worst Case: As with the best and average cases, the worst case scenario does not change. Matrix multiplication requires a fixed number of operations based on the sizes of the matrices, and thus the time complexity is again O(rows_A * cols_B * cols_A).
