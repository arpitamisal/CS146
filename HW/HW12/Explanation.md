Kruskal's Algorithm with Union-Find
Graph Modeling: Treat each house as a node. Model connections between houses and well-building costs as edges, including edges from a virtual node to houses for well costs.
Union-Find: Utilize union-find to manage and merge node sets efficiently, ensuring no cycles while achieving minimum cost connectivity.
Execution:
Collect and sort all edges by cost (pipes and wells).
Use the union-find to add edges to the Minimum Spanning Tree (MST), selecting edges in ascending cost order and avoiding cycles.
