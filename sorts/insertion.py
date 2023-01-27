import time
import random
import threading
import math

def insertion_sort(array, main, stop):
    n = len(array)
    for i in range(1, n):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
            main.event_generate("<<draw>>")
            time.sleep(0.001)
            if stop[0]:
                return