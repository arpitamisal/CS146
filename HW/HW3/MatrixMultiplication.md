MATRIX_MULTIPLY(A, B):
if columns(A) ≠ rows(B):
raise ValueError("Matrix multiplication is not defined.")

    rows_A ← number of rows in A
    cols_A ← number of columns in A
    cols_B ← number of columns in B
    result ← matrix of size rows_A x cols_B filled with zeros

    for i from 1 to rows_A do:
        for j from 1 to cols_B do:
            sum ← 0
            for k from 1 to cols_A do:
                sum ← sum + A[i][k] * B[k][j]
            result[i][j] ← sum
    return result

Time Complexity Analysis

    Time Complexity: The time complexity is determined by the three nested loops. Each loop iterates up to the size of the dimensions of the input matrices:
        The outer loop runs for each row in A (rows_A times),
        The middle loop runs for each column in B (cols_B times),
        The inner loop runs for each column in A, which is also the number of rows in B (cols_A or rows_B times).
    Thus, the total number of operations is rows_A * cols_B * cols_A, leading to a time complexity of O(n^3) for square matrices of size n x n.
    Space Complexity: O(rows_A * cols_B) due to the space required to store the result matrix.
