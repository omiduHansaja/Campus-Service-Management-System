import csv
import time
import math


# Function to read location data
def read_locations(filename):
    locations = []

    file = open(filename, "r")
    reader = csv.DictReader(file)

    # Store each record read as dictionaries
    for row in reader:
        location = {
            "LocationID": row["LocationID"],
            "x": float(row["X"]),
            "y": float(row["Y"])
        }
        locations.append(location)

    file.close()
    return locations


# Function to calculate distance using X and Y co-ordinates
def calculate_distance(point_a, point_b):
    dx = point_a["x"] - point_b["x"]
    dy = point_a["y"] - point_b["y"]
    return math.sqrt(dx * dx + dy * dy)


# Function for Greedy nearest-neighbour algorithm
def greedy_nearest_route(locations, start):
    visited_points = []  # List to store visited locations
    unvisited_points = locations.copy()
    current_location = start
    total_distance = 0

    # Start from the initial Location
    visited_points.append(current_location)
    unvisited_points.remove(current_location)

    # Continue until all locations are visited
    while len(unvisited_points) > 0:
        next_point = unvisited_points[0]
        nearest_distance = calculate_distance(current_location, next_point)

        # Find the closest unvisited point(location)
        for loc in unvisited_points:
            dist = calculate_distance(current_location, loc)
            if dist < nearest_distance:
                next_point = loc
                nearest_distance = dist

        # Move to the closest location
        visited_points.append(next_point)
        unvisited_points.remove(next_point)
        total_distance += nearest_distance
        current_location = next_point

    return visited_points, total_distance


# Dijkstra's algorithm
def dijkstra_route(locations, start):
    distances = {}  # Stores the shortest distances to each location
    visited_points = []  # List to store visited location ID's
    previous_points = {}  # Stores previous locations for each point

    # Store distances for each location
    for loc in locations:
        distances[loc["LocationID"]] = float("inf")
        previous_points[loc["LocationID"]] = None

    distances[start["LocationID"]] = 0

    # Continue until all locations(points) are visited
    while len(visited_points) < len(locations):
        current = None
        current_distance = float("inf")

        # Select the unvisited location with shortest distance
        for loc in locations:
            if loc["LocationID"] not in visited_points:
                if distances[loc["LocationID"]] < current_distance:
                    current = loc
                    current_distance = distances[loc["LocationID"]]

        visited_points.append(current["LocationID"])

        # Update distances to near locations
        for loc in locations:
            if loc["LocationID"] not in visited_points:
                dist = calculate_distance(current, loc)
                new_distance = distances[current["LocationID"]] + dist

                if new_distance < distances[loc["LocationID"]]:
                    distances[loc["LocationID"]] = new_distance
                    previous_points[loc["LocationID"]] = current["LocationID"]

    return distances


# Load location.csv
locations = read_locations("campus_data/locations.csv")
start_location = locations[0]

print("**************************************")
print(" Route Optimisation ")
print("**************************************")

# Run Greedy Nearest-Neighbour algorithm
start_time = time.time()
route, distance = greedy_nearest_route(locations, start_location)
greedy_time = (time.time() - start_time) * 1000

print("======================================")
print("Greedy Nearest-Neighbour Route: ")

for loc in route:
    print(loc["LocationID"], end=" -> ")
print()

print("Total Distance: ", round(distance, 2))
print("Computation Time: ", round(greedy_time, 3), "ms")
print()
print("======================================")

# Run Dijkstra's algorithm
start_time = time.time()
distances = dijkstra_route(locations, start_location)
dijkstra_time = (time.time() - start_time) * 1000

print("======================================")
print("Dijkstra Shortest Distances from", start_location["LocationID"], ":")
for loc_id in distances:
    print(loc_id, ":", round(distances[loc_id], 2))

print("Computation Time: ", round(dijkstra_time, 3), "ms")
print(" ")
print("======================================")
