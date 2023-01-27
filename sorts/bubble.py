import time
import random
import threading
import math

def bubble_sort(array, main, stop):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                main.event_generate("<<draw>>")
                time.sleep(0.001)
            if stop[0]:
                return