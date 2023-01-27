import time
import random
import threading
import math

def shell_sort(array, main, stop):
    n = len(array)
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, n):
            tmp = array[i]
            j = i
            while j >= gap and array[j - gap] > tmp:
                array[j] = array[j - gap]
                j -= gap
                main.event_generate("<<draw>>")
                time.sleep(0.001)
                if stop[0]:
                    return
            array[j] = tmp
            main.event_generate("<<draw>>")
            time.sleep(0.001)