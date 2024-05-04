for i from 1 to length(A){
key ← A[i]
j ← i - 1
while j >= 0 and A[j] > key {
A[j + 1] ← A[j]
j ← j - 1
}
A[j + 1] ← key
}

Time Complexity Analysis

    Best Case: When the array is already sorted, the inner loop does no work (i.e., A[j] > key is false on the first check), so the algorithm runs in O(n) time.
    Average and Worst Case: For each i from 1 to n-1, the worst case occurs when the array is reverse sorted, and we have to compare each element with all the other elements already sorted. Thus, we perform n-1, n-2, ..., 1, 0 comparisons, leading to a time complexity of O(n^2).
    Space Complexity: O(1) as it is an in-place sorting algorithm.
