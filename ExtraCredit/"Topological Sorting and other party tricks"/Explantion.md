# Kahn's Algorithm (Using BFS)

It starts by calculating the in-degree (number of incoming edges) for each vertex. All vertices with an in-degree of zero are added to a queue. As each vertex is processed (dequeued), it's added to the topological order, and its neighbors' in-degrees are decreased by one. If a neighbor's in-degree drops to zero, it's added to the queue.

# Kahn's Algorithm (Using DFS)

It uses a recursive depth-first search (DFS) to explore each vertex and its descendants. As each vertex's exploration is completed, the vertex is pushed onto a stack. This ensures that a vertex is only placed in the sorted order after all vertices depending on it have been placed.
