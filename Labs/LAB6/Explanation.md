We can determine if all courses can be finished given their prerequisites by using a topological sorting approach with Kahn's Algorithm. Here’s the logic followed in the solution:
Graph Representation: Start modeling the courses and prerequisites as a directed graph, where each course points to other courses that depend on it, and then track the number of prerequisites each course has using an indegree array.
Queue Initialization: Then, initialize a queue with courses that have no prerequisites (indegree of zero), as these can be taken immediately.
Processing the Queue: Dequeue a course, add it to the result list, and for each course that depends on the dequeued course, reduce its indegree by one. If this results in a course having zero prerequisites, enqueue it.
Completion Check: After processing, if the number of courses in the result list equals the total number of courses, all courses can be completed. Otherwise, a cycle exists, preventing some courses from being completed.
