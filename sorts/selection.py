import time
import random
import threading
import math

def selection_sort(array, main, stop):
    n = len(array)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if (array[j] < array[min_idx]):
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
        main.event_generate("<<draw>>")
        time.sleep(0.001)
        if stop[0]:
            return