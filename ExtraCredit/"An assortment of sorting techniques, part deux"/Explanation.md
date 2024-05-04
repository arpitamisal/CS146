Properties of Heaps:

    A heap is a complete binary tree.
    Every node follows the heap property; for a max heap, each parent node is greater than or equal to its child nodes, and for a min heap, each parent node is less than or equal to its child nodes.

Heap as Priority Queue:

    Insertion: When a new element is added, it is initially placed at the end of the heap. The heap property is restored by comparing the added element with its parent and moving it up the heap (heapify up or bubble up) until the correct position is found. This operation is O(log⁡n)O(logn) in complexity.
    Deletion/Access of Top Element: The top element (maximum in max heap, minimum in min heap) can be accessed in constant time, O(1)O(1). Removing the top element involves replacing it with the last element in the heap and then restoring the heap property by pushing this element down the heap (heapify down or bubble down). This is also O(log⁡n)O(logn).

Pseudocode for Insertion in a Max Heap:

function insert(value):
heap.append(value)
index = heap.size() - 1
while index > 0 and heap[parent(index)] < heap[index]:
swap(heap[parent(index)], heap[index])
index = parent(index)

Pseudocode for Removing Top Element in a Max Heap:

function extractMax():
if heap.size() == 0:
return null
max_value = heap[0]
heap[0] = heap.pop()
heapifyDown(0)
return max_value

function heapifyDown(index):
left = leftChild(index)
right = rightChild(index)
largest = index
if left < heap.size() and heap[left] > heap[largest]:
largest = left
if right < heap.size() and heap[right] > heap[largest]:
largest = right
if largest != index:
swap(heap[index], heap[largest])
heapifyDown(largest)

It is possible to use a max heap as a min heap by inverting the priority of the elements. This is done by inserting the negative of the actual values when dealing with integers (or using a custom comparator that inverts the comparison). The extracted value must be negated back to return the correct value. The opposite is true for using a min heap as a max heap.

Python Example using Max Heap as Min Heap:
import heapq

max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)

min_value = -heapq.heappop(max_heap)
print(min_value) # Output will be 1, the smallest element

This approach allows using the same heap implementation for both min and max priorities by simply inverting the values during insertion and extraction. This is efficient and avoids the need to implement separate heap structures for different types of priority queues.

By using this method, we can effectively utilize heaps as versatile priority queues for a variety of applications where elements need to be processed in a specific order dictated by their priorities.
