import time
import random
import threading
import math

def heapify(arr, N, i, stop):
    if (stop[0]):
            return
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, N, largest, stop)

def heap_sort(array, main, stop):

    N = len(array)

    for i in range(N//2 - 1, -1, -1):
        heapify(array, N, i, stop)
        main.event_generate("<<draw>>")
        if (stop[0]):
            return

    for i in range(N-1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        heapify(array, i, 0, stop)
        main.event_generate("<<draw>>")
        if (stop[0]):
            return