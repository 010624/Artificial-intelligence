from queue import PriorityQueue

# A* Heuristic function: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar_search(graph, start, goal):
    # Priority queue for the frontier
    frontier = PriorityQueue()
    frontier.put((0, start))

    # Stores the best path cost from the start to each node
    came_from = {}
    cost_so_far = {}

    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current_priority, current_node = frontier.get()

        # If we reached the goal
        if current_node == goal:
            break

        # Explore neighbors
        for next_node in graph[current_node]:
            new_cost = cost_so_far[current_node] + graph[current_node][next_node]

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(goal, next_node)  # f(n) = g(n) + h(n)
                frontier.put((priority, next_node))
                came_from[next_node] = current_node

    return came_from, cost_so_far

# Reconstruct the path from start to goal
def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# Example graph: A 2D grid with weights
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1, (2, 1): 1},
    (2, 0): {(1, 0): 1, (2, 1): 1},
    (2, 1): {(1, 1): 1, (2, 0): 1}
}

# Start and goal positions
start = (0, 0)
goal = (2, 1)

# Run A* algorithm
came_from, cost_so_far = astar_search(graph, start, goal)
path = reconstruct_path(came_from, start, goal)

# Output the result
print(f"Path: {path}")
print(f"Total Cost: {cost_so_far[goal]}")

