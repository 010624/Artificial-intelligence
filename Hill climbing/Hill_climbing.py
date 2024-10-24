import random

# Objective function
def objective_function(x):
    return -(x ** 2) + 5  # Example function (you can replace this with any other function)

# Hill Climbing algorithm with path tracking
def hill_climbing(objective_function, start_point, step_size, max_iterations):
    # Initialize the current point and its value
    current_point = start_point
    current_value = objective_function(current_point)
    
    # Track the optimal path and distances
    path = [(current_point, current_value)]
    total_distance = 0

    for iteration in range(max_iterations):
        # Generate a neighbor by taking a small step
        next_point = current_point + random.uniform(-step_size, step_size)
        next_value = objective_function(next_point)

        # Calculate the distance from current point to the next point
        distance = abs(next_point - current_point)

        # If the neighbor is better, move to the neighbor
        if next_value > current_value:
            current_point = next_point
            current_value = next_value
            total_distance += distance
            path.append((current_point, current_value))  # Track the path

        print(f"Iteration {iteration+1}: Current Point = {current_point}, Current Value = {current_value}, Distance = {distance}")

    return current_point, current_value, path, total_distance

# Parameters
start_point = random.uniform(-10, 10)
step_size = 0.1
max_iterations = 100

# Run Hill Climbing
best_point, best_value, optimal_path, total_distance = hill_climbing(objective_function, start_point, step_size, max_iterations)

# Output the result
print(f"\nBest Point: {best_point}, Best Value: {best_value}")
print(f"Optimal Path: {optimal_path}")
print(f"Total Distance Traveled: {total_distance}")

