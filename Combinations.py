from math import comb

def count_traffic_route_combinations(n, k):
    return comb(n, k)

# Example usage:
num_routes = 10
num_selected_routes = 3
combinations = count_traffic_route_combinations(num_routes, num_selected_routes)
print("Number of combinations of traffic routes:", combinations)
