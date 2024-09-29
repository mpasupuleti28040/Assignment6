# Implementing the Algorithms
def median_of_medians(arr, k):
    # If the list contains 5 or fewer elements, return the k-th smallest directly after sorting
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # Partition the array into sublists of 5 elements each and find the median of each sublist
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Recursively apply the algorithm to the list of medians to find the pivot
    pivot = median_of_medians(medians, len(medians) // 2 + 1)

    # Partition the array based on the pivot and apply recursive selection to the appropriate partition
    low = [el for el in arr if el < pivot]
    high = [el for el in arr if el > pivot]
    count = arr.count(pivot)

    if k <= len(low):
        return median_of_medians(low, k)
    elif k > len(low) + count:
        return median_of_medians(high, k - len(low) - count)
    else:
        return pivot

import random

def quickselect(arr, k):
    # If the array has only one element, return it
    if len(arr) == 1:
        return arr[0]

    # Randomly select a pivot
    pivot = random.choice(arr)

    # Partition the array into elements smaller, equal, and greater than the pivot
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k <= len(lows):
        return quickselect(lows, k)
    elif k > len(lows) + len(pivots):
        return quickselect(highs, k - len(lows) - len(pivots))
    else:
        return pivots[0]


# Empirical Testing and Runtime Analysis

import time

def measure_performance(selection_algorithm, array, k):
    start_time = time.time()
    result = selection_algorithm(array.copy(), k)
    end_time = time.time()
    return end_time - start_time, result

def benchmark_algorithms():
    # Generate test arrays
    random_array = [random.randint(1, 1000) for _ in range(1000)]
    sorted_array = sorted(random_array)
    reverse_sorted_array = sorted_array[::-1]
    k = 500  # We are interested in the 500th smallest element

    # Measure performance of quickselect
    print("Quickselect Performance:")
    time_taken, result = measure_performance(quickselect, random_array, k)
    print(f"Random array: {time_taken} seconds, Result: {result}")
    
    time_taken, result = measure_performance(quickselect, sorted_array, k)
    print(f"Sorted array: {time_taken} seconds, Result: {result}")
    
    time_taken, result = measure_performance(quickselect, reverse_sorted_array, k)
    print(f"Reverse sorted array: {time_taken} seconds, Result: {result}")

    # Measure performance of median_of_medians
    print("\nMedian of Medians Performance:")
    time_taken, result = measure_performance(median_of_medians, random_array, k)
    print(f"Random array: {time_taken} seconds, Result: {result}")
    
    time_taken, result = measure_performance(median_of_medians, sorted_array, k)
    print(f"Sorted array: {time_taken} seconds, Result: {result}")
    
    time_taken, result = measure_performance(median_of_medians, reverse_sorted_array, k)
    print(f"Reverse sorted array: {time_taken} seconds, Result: {result}")

benchmark_algorithms()
