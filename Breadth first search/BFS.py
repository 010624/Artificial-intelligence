from collections import deque

# Breadth-First Search (BFS) algorithm
def bfs(graph, start, goal):
    # Queue to manage the frontier, initializing with the start node
    queue = deque([[start]])
    
    # Set to track visited nodes
    visited = set([start])

    while queue:
        # Get the current path from the queue
        path = queue.popleft()
        node = path[-1]

        # If we reached the goal, return the path
        if node == goal:
            return path

        # Explore neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Add the neighbor to the path and queue
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                # Mark the neighbor as visited
                visited.add(neighbor)

    return None  # Return None if no path found

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Define the start and goal nodes
start = 'A'
goal = 'F'

# Run BFS
path = bfs(graph, start, goal)

# Output the result
if path:
    print(f"Path from {start} to {goal}: {path}")
else:
    print(f"No path found from {start} to {goal}")
