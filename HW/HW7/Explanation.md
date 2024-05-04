To solve this problem, we first sort the job intervals based on their start times. This allows us to systematically assign servers to jobs in the order they begin. We employ a min-heap (priority queue) to keep track of when each server becomes free. The key operations are:

- Inserting an end time into the heap
- Removing the minimum end time from the heap
