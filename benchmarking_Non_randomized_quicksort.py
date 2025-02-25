import matplotlib.pyplot as plt
import random
import timeit
import numpy as np
def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r] = A[i]
    return partition(A, p, r)
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def Non_randomized_quicksort(A,p,r):
    if p < r:
        q=randomized_partition(A,p,r)
        Non_randomized_quicksort(A,p,q-1)
        Non_randomized_quicksort(A,q+1,r)

def generate_random_array(size):
    # Generate a random array of integers for a given size
    return [random.randint(0, 99999) for i in range(size)]

def generate_sorted_array(size):
    return [i for i in range(size)]

# Generate a reverse sorted array
def generate_reverse_sorted_array(size):
    return [i for i in range(size, 0, -1)]

def calculate_benchmark_algorithm(number_of_runs):
    sizes = []
    quicksort_besttimes = []
    quicksort_avgtimes = []
    quicksort_worsttimes = []
    for i in range(number_of_runs):
        # Generate a random array with a random size
        size = random.randint(0, 8) # Random size between 0 and 10, we can change the numbers as needed
        arr = generate_random_array(size)  # Generate an array of the randomly generated size
        print("Generated array: of size: ", arr, size)

    # Generate best, worst, and average cases based on array size
        best_case_input = sorted(arr)  # Sorted array (best case)
        worst_case_input =sorted(arr,reverse=True)  # Reverse sorted array (worst case)
        avg_case_input = arr # Random array (average case)
        print(f"array used for best_case_input {best_case_input}")
        print(f"array used for worst_case_input{worst_case_input}")
        print(f"array used for avg_case_input{avg_case_input}")
        best_time = timeit.timeit(lambda:  Non_randomized_quicksort(best_case_input.copy(), 0, len(best_case_input) - 1), number=1)
        avg_time = timeit.timeit(lambda:  Non_randomized_quicksort(avg_case_input.copy(), 0, len(avg_case_input) - 1), number=1)
        worst_time = timeit.timeit(lambda: Non_randomized_quicksort(worst_case_input.copy(), 0, len(worst_case_input) - 1), number=1)
        print(f"time taken for quicksort best case {best_time}, "
               f" for quick sort avg case: {avg_time} "
               f" for quick sort worst case: {worst_time}"
               f" for original array {arr} of size {size}")
        sizes.append(size)
        quicksort_besttimes.append(best_time)
        quicksort_avgtimes.append(avg_time)
        quicksort_worsttimes.append(worst_time)

    return sizes, quicksort_besttimes, quicksort_avgtimes,quicksort_worsttimes

number_of_runs =10# You can change this to test more random number of times
time_for_diff_sorting_algos = calculate_benchmark_algorithm(number_of_runs)

# Sort the data based on input sizes for better line plotting
sorted_indices = np.argsort(time_for_diff_sorting_algos[0])  # Sort based on sizes
sizes_sorted = np.array(time_for_diff_sorting_algos[0])[sorted_indices]
best_case_sorted = np.array(time_for_diff_sorting_algos[1])[sorted_indices]
avg_case_sorted = np.array(time_for_diff_sorting_algos[2])[sorted_indices]
worst_case_sorted = np.array(time_for_diff_sorting_algos[3])[sorted_indices]
print(f"Sizes and times after sorting:{sizes_sorted}, {best_case_sorted}, {avg_case_sorted}, {worst_case_sorted}")
# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sizes_sorted, best_case_sorted, label="Best case", marker='x')
plt.plot(sizes_sorted, avg_case_sorted, label="Avg Sort", marker='o')
plt.plot(sizes_sorted,worst_case_sorted, label="Worst Sort", marker='^')
plt.xlabel('arraysize')
plt.ylabel('Time (seconds)')
plt.title('Benchmarking  Quick Sorting Algorithms with different cases')
plt.legend()
plt.grid(True)
plt.show()

