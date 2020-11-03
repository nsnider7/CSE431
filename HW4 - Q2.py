import time
import matplotlib.pyplot as plt
import random


# Insertion sort
# Implementation from https://www.geeksforgeeks.org/python-program-for-insertion-sort/
# Function to do insertion sort
def insertionSortRegular(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


#
# Merge Sort
# Implementation from https://www.geeksforgeeks.org/python-program-for-merge-sort/
def mergeHelper(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# Hybrid sort based off of below merge sort
def timSort(arr, l, r, k):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        if len(arr) < k:
            insertionSortRegular(arr)
        else:
            timSort(arr, l, m, k)
            timSort(arr, m + 1, r, k)
        mergeHelper(arr, l, m, r)


def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        mergeHelper(arr, l, m, r)


insertion_times = []
merge_times = []
tim_times = []
list_lengths = []
k = 120  # can change this value of k manually to test other vlaues
# insertion sort
for i in range(150):
    list_lengths.append(i)
    insertion_random = []
    merge_random = []
    tim_random = []
    # put random values into each list
    for i in range(0, i):
        n = random.randint(0, 150)
        insertion_random.append(n)
        merge_random.append(n)
        tim_random.append(n)
    # measure time for merge sort on this list
    start2 = time.perf_counter()
    mergeSort(merge_random, 0, len(merge_random) - 1)
    end2 = time.perf_counter()
    merge_time = end2 - start2
    merge_times.append(merge_time)

    # measure time for insertion sort on this list
    start1 = time.perf_counter()
    insertionSortRegular(insertion_random)
    end1 = time.perf_counter()
    insertion_time = end1 - start1
    insertion_times.append(insertion_time)

    # measure time for insertion sort on this list
    start3 = time.perf_counter()
    timSort(tim_random, 0, len(merge_random) - 1, k)
    end3 = time.perf_counter()
    time_time = end3 - start3
    tim_times.append(time_time)

plt.plot(list_lengths, insertion_times, color="blue", label="Insertion Sort")
plt.plot(list_lengths, merge_times, color="olive", label="Merge Sort")
plt.plot(list_lengths, tim_times, color="red", label="Tim Sort")
plt.xlabel('List lengths')
plt.ylabel('Time (sec)')
plt.show()
