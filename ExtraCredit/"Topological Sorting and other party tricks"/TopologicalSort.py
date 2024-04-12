from collections import deque


# Kahn's Algorithm (Using BFS)
def kahns_algorithm(num_courses, prerequisites):
    indegree = [0] * num_courses
    graph = {i: [] for i in range(num_courses)}

    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1

    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    topo_sort = []

    while queue:
        vertex = queue.popleft()
        topo_sort.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_sort) == num_courses:
        return topo_sort
    else:
        return []  # not possible to sort as the graph has a cycle


# Kahn's Algorithm (Using DFS)
def topological_sort_dfs(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for dest, src in prerequisites:
        graph[src].append(dest)

    visited = [False] * num_courses
    stack = []
    cycle = [False] * num_courses  # To detect cycle in the graph

    def dfs(vertex):
        if cycle[vertex]:
            return False
        if visited[vertex]:
            return True

        visited[vertex] = True
        cycle[vertex] = True
        for neighbor in graph[vertex]:
            if not dfs(neighbor):
                return False
        cycle[vertex] = False
        stack.append(vertex)
        return True

    for course in range(num_courses):
        if not visited[course]:
            if not dfs(course):
                return []  # not possible to sort as the graph has a cycle

    return stack[::-1]


# Sample Input and Output
num_courses = 5
prerequisites = [(1, 0), (2, 0), (3, 1), (4, 2), (4, 3)]

print("Kahn's Algorithm:", kahns_algorithm(num_courses, prerequisites))
print("DFS:", topological_sort_dfs(num_courses, prerequisites))

# Graph
#            0
#          ↓    ↘
#          1     2
#          ↓     ↓
#          3  →  4
