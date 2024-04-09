### 1. Converting an Adjacency List to an Adjacency Matrix ###

# Pseudocode #
""" function adjListToMatrix(adjList):
    matrixSize = length of adjList
    initialize matrix with size matrixSize x matrixSize filled with zeros 
  
    for each vertex in adjList:
        for each neighbor in adjList[vertex]:
            matrix[vertex][neighbor] = 1
           
    return matrix
"""


# Code #
def adjListToMatrix(adjList):
    matrixSize = len(adjList)
    matrix = [[0] * matrixSize for _ in range(matrixSize)]

    for vertex, neighbors in enumerate(adjList):
        for neighbor in neighbors:
            matrix[vertex][neighbor] = 1

    return matrix


# Explation #
""" 
An adjacency list represents each vertex and its neighbors. To convert this 
into a matrix, we will have to create a 2D array with a size of V x V where V 
is the number of vertices. Then initialize the matrix with zeros. For each vertex,
go through its adjacency list and set the corresponding matrix cell to 1.
"""


### 2. Converting an Adjacency Matrix to an Adjacency List ###

# Pseudocode #
"""
function adjMatrixToList(matrix):
    initialize adjList with length of matrix rows
    
    for i from 0 to length of matrix:
        for j from 0 to length of matrix[i]:
            if matrix[i][j] is 1:
                add j to adjList[i]
                
    return adjList
"""


# Code #
def adjMatrixToList(matrix):
    adjList = [[] for _ in range(len(matrix))]

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 1:
                adjList[i].append(j)

    return adjList


# Explation #
"""
An adjacency matrix represents the graph where each cell (i, j) is 1 if there 
is an edge from vertex 'i' to 'j'. To convert it to a list, we iterate through the matrix 
and for each '1' found in row 'i', add 'j' to the adjacency list of 'i'.
"""

### 3. Reversing a Directed Graph ###

# Pseudocode #
"""
function reverseGraph(adjList):
    initialize newAdjList with length of adjList
    
    for each vertex in adjList:
        for each neighbor in adjList[vertex]:
            add vertex to newAdjList[neighbor]
            
    return newAdjList
"""


# Code #
def reverseGraph(adjList):
    newAdjList = [[] for _ in range(len(adjList))]

    for vertex, neighbors in enumerate(adjList):
        for neighbor in neighbors:
            newAdjList[neighbor].append(vertex)

    return newAdjList


# Explation #
"""
To reverse the graph, for every directed edge from 'u' to 'v', we create an edge
from 'v' to 'u' in the new graph. If given an adjacency list, we create a
new list and insert 'u' into the list at index 'v'.
"""
