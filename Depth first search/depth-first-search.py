# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Iterative DFS function
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]  # Use a stack to manage the order of exploration

    while stack:
        node = stack.pop()  # Take the last element (LIFO order)
        
        if node not in visited:
            print(node, end=" ")  # Process the node (e.g., print it)
            visited.add(node)

            # Add unvisited neighbors to the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Run DFS starting from node 'A'
dfs_iterative(graph, 'A')
