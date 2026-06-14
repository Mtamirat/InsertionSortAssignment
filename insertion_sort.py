import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

small_array = [5, 2, 9, 1, 5, 6]

large_array = [random.randint(1, 10000) for _ in range(1000)]

nearly_sorted_array = list(range(1000))
nearly_sorted_array[998], nearly_sorted_array[999] = (
    nearly_sorted_array[999],
    nearly_sorted_array[998]
)

reversed_array = list(range(1000, 0, -1))

print("Small Array:")
print(insertion_sort(small_array.copy()))

print("\nLarge Array Sorted Successfully:",
      insertion_sort(large_array.copy()) == sorted(large_array))

print("Nearly Sorted Array Sorted Successfully:",
      insertion_sort(nearly_sorted_array.copy()) == sorted(nearly_sorted_array))

print("Reversed Array Sorted Successfully:",
      insertion_sort(reversed_array.copy()) == sorted(reversed_array))

def measure_time(arr):
    start = time.perf_counter()
    insertion_sort(arr.copy())
    end = time.perf_counter()
    return end - start

print("\nTiming Results")
print("Nearly Sorted:", measure_time(nearly_sorted_array))
print("Reversed:", measure_time(reversed_array))