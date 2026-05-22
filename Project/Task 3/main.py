import csv
import time
import tracemalloc
import matplotlib.pyplot as plt

# importing files
from sorting_algorithms.bubbleSort import bubble_sort
from sorting_algorithms.mergeSort import merge_sort
from searching_algorithms.linearSearch import linear_search
from searching_algorithms.binarySearch import binary_search


# Function to onvert priority levels into numbers
def priority_number(priority):
    priority = priority.lower()
    if priority == "high":
        return 3
    elif priority == "medium":
        return 2
    else:
        return 1


# Function to read all requests from a CSV file
def read_requests(filename):
    data = []

    # Open the file in read mode
    file = open(filename, "r")
    reader = csv.DictReader(file)

    # Read each row(record) and store it as a dictionary
    for row in reader:
        request_record = {
            "RequestId": row["RequestId"],
            "LocationId": row["LocationId"],
            "ServiceType": row["ServiceType"],
            "Priority": priority_number(row["Priority"]),
            "RequestDate": row["RequestDate"],
            "RequestTime": row["RequestTime"]
        }
        data.append(request_record)

    file.close()
    return data


# Function to run sorting algorithms
def run_sort(algorithm, data):
    tracemalloc.start()
    start = time.time()

    sorted_data, comparisons = algorithm(data.copy())
    time_taken = (time.time() - start) * 1000  # Converting to milliseconds

    current_memory, max_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()
    return sorted_data, comparisons, time_taken, max_memory / 1024


# Function to run searching algorithms
def run_search(algorithm, data, target_record):
    tracemalloc.start()
    start = time.time()

    is_found, comparisons = algorithm(data, target_record)
    time_taken = (time.time() - start) * 1000
    current_memory, max_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()
    return comparisons, time_taken, max_memory / 1024


# List to store CSV files
test_files = [
    "test_data/requests_100.csv",
    "test_data/requests_300.csv",
    "test_data/requests_500.csv"
]

# Dataset sizes for graphs
file_sizes = [100, 300, 500]

# Lists to store execution times
bubble_times = []
merge_times = []
linear_times = []
binary_times = []

# Lists to store comparisons
bubble_comparisons = []
merge_comparisons = []
linear_comparisons = []
binary_comparisons = []

# Lists to store memory usage
bubble_memory = []
merge_memory = []
linear_memory = []
binary_memory = []


# Iterate through each dataset
for file_name in test_files:
    print(" ")
    print("========================================")
    print("Input File: ", file_name)

    data = read_requests(file_name)
    target = data[len(data) // 2]

    print("****************************************")
    print(" Performance Metrics ")
    print("****************************************")

    # Bubble Sort
    sorted_data, comp, time_taken, memory = run_sort(bubble_sort, data)

    time_taken = round(time_taken, 6)
    memory = round(memory, 6)

    bubble_times.append(time_taken)
    bubble_comparisons.append(comp)
    bubble_memory.append(memory)

    print(" Bubble Sort --> Time: ", time_taken, "ms || Comparisons: ",
          comp, " || Memory usage: ", memory, "KB")

    # Merge Sort
    sorted_data, comp, time_taken, memory = run_sort(merge_sort, data)

    # to only take 6 numbers after decimal point
    time_taken = round(time_taken, 6)
    memory = round(memory, 6)

    merge_times.append(time_taken)
    merge_comparisons.append(comp)
    merge_memory.append(memory)
    print(" Merge Sort --> Time: ", time_taken, "ms || Comparisons: ",
          comp, " || Memory usage: ", memory, "KB")

    # Linear Search
    comp, time_taken, memory = run_search(linear_search, data, target)

    time_taken = round(time_taken, 6)
    memory = round(memory, 6)

    linear_times.append(time_taken)
    linear_comparisons.append(comp)
    linear_memory.append(memory)
    print(" Linear Search --> Time: ", time_taken, "ms || Comparisons: ",
          comp, " || Memory usage: ", memory, "KB")

    # Binary Search
    comp, time_taken, memory = run_search(binary_search, sorted_data, target)

    time_taken = round(time_taken, 6)
    memory = round(memory, 6)

    binary_times.append(time_taken)
    binary_comparisons.append(comp)
    binary_memory.append(memory)
    print(" Binary Search --> Time: ", time_taken, "ms || Comparisons: ",
          comp, " || Memory usage: ", memory, "KB")

    print("****************************************")


# Execution time graphs
plt.figure()
plt.plot(file_sizes, bubble_times, marker="o", label="Bubble Sort")
plt.plot(file_sizes, merge_times, marker="o", label="Merge Sort")
plt.title("Sorting Algorithms – Execution Time")
plt.xlabel("Number of Requests")
plt.ylabel("Time (ms)")
plt.legend()
plt.show()

plt.figure()
plt.plot(file_sizes, linear_times, marker="o", label="Linear Search")
plt.plot(file_sizes, binary_times, marker="o", label="Binary Search")
plt.title("Searching Algorithms – Execution Time")
plt.xlabel("Number of Requests")
plt.ylabel("Time (ms)")
plt.legend()
plt.show()


# Comparison count graphs
plt.figure()
plt.plot(file_sizes, bubble_comparisons, marker="o", label="Bubble Sort")
plt.plot(file_sizes, merge_comparisons, marker="o", label="Merge Sort")
plt.title("Sorting Algorithms – Number of Comparisons")
plt.xlabel("Number of Requests")
plt.ylabel("Comparisons")
plt.legend()
plt.show()

plt.figure()
plt.plot(file_sizes, linear_comparisons, marker="o", label="Linear Search")
plt.plot(file_sizes, binary_comparisons, marker="o", label="Binary Search")
plt.title("Searching Algorithms – Number of Comparisons")
plt.xlabel("Number of Requests")
plt.ylabel("Comparisons")
plt.legend()
plt.show()


# Memory usage graphs
plt.figure()
plt.plot(file_sizes, bubble_memory, marker="o", label="Bubble Sort")
plt.plot(file_sizes, merge_memory, marker="o", label="Merge Sort")
plt.title("Sorting Algorithms – Memory Usage")
plt.xlabel("Number of Requests")
plt.ylabel("Memory (KB)")
plt.legend()
plt.show()

plt.figure()
plt.plot(file_sizes, linear_memory, marker="o", label="Linear Search")
plt.plot(file_sizes, binary_memory, marker="o", label="Binary Search")
plt.title("Searching Algorithms – Memory Usage")
plt.xlabel("Number of Requests")
plt.ylabel("Memory (KB)")
plt.legend()
plt.show()
