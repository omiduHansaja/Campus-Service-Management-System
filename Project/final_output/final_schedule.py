import csv
import math


# Function to load requests from the csv file
def load_requests(filename):
    request_list = []
    file = open(filename, "r")
    reader = csv.DictReader(file)

    # Store each request read as a dictionary
    for row in reader:
        request_list.append({
            "RequestID": row["RequestID"],
            "LocationID": row["LocationID"],
            "ServiceType": row["ServiceType"]
        })

    file.close()
    return request_list


# Function to load staff data from the csv file
def load_staff(filename):
    staff_list = []
    file = open(filename, "r")
    reader = csv.DictReader(file)

    for row in reader:
        staff_list.append({
            "StaffID": row["StaffID"],
            "Role": row["Role"],
            "MaxTasksPerDay": int(row["MaxTasksPerDay"]),
            "Assigned": 0  # To keep count for assigned tasks
        })

    file.close()
    return staff_list


# Function to load location data from the csv file
def load_locations(filename):
    location_list = []
    file = open(filename, "r")
    reader = csv.DictReader(file)

    for row in reader:
        location_list.append({
            "LocationID": row["LocationID"],
            "x": float(row["X"]),
            "y": float(row["Y"])
        })

    file.close()
    return location_list


# Function to Calculate the distance
def calculate_distance(a, b):
    dx = a["x"] - b["x"]
    dy = a["y"] - b["y"]
    return math.sqrt(dx * dx + dy * dy)


# Function to perform greedy algorithm
def greedy_route(locations, start, target):
    unvisited = locations.copy()
    current = start
    route = [current["LocationID"]]
    total_distance = 0

    # Remove the starting point from unvisited list
    for location in unvisited:
        if location["LocationID"] == start["LocationID"]:
            unvisited.remove(location)
            break

    # Continue until the target location(point)
    while current["LocationID"] != target["LocationID"]:
        nearest = None
        nearest_distance = float("inf")

        # Find the closest unvisited point
        for loc in unvisited:
            d = calculate_distance(current, loc)
            if d < nearest_distance:
                nearest = loc
                nearest_distance = d

        # Move to the nearest point
        route.append(nearest["LocationID"])
        total_distance += nearest_distance
        current = nearest
        unvisited.remove(nearest)

    return route, total_distance


# Load data files
requests = load_requests("campus_data/requests.csv")
staff = load_staff("campus_data/staff.csv")
locations = load_locations("campus_data/locations.csv")

# Defining the starting location
start_point = locations[0]

print("**************************************")
print(" Final Service Schedule ")
print("**************************************")


# Assigns each request to the available staff member
for request in requests:

    # Find the available staff member
    assigned_staff = None
    for staff_member in staff:
        if staff_member["Assigned"] < staff_member["MaxTasksPerDay"]:
            assigned_staff = staff_member
            staff_member["Assigned"] += 1
            break

    # Find the location related to request
    request_location = None
    for loc in locations:
        if loc["LocationID"] == request["LocationID"]:
            request_location = loc
            break

    # Generate an optimized route to the request location
    route, total_distance = greedy_route(
        locations, start_point, request_location)

    # Display the output for the final schedule
    print("Request ID: ", request["RequestID"])
    print("Staff ID: ", assigned_staff["StaffID"])
    print("Location ID: ", request_location["LocationID"])

    print("Route: ", end=" ")

    for i in range(len(route)):
        print(route[i], end="")
        if i < len(route) - 1:
            print(" -> ", end="")
    print()
    
    print("Distance Travelled: ", round(total_distance, 2))
    print("=====================================")
