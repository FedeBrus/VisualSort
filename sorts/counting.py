import time
import random
import threading
import math

def counting_sort(array, main, stop):
    maxA = (max(array) + 1)
    copia = [0] * maxA

    for x in array:
        copia[x] = copia[x] + 1
        if (stop[0]):
            return

    j = 0
    for i in range(maxA):
        while (copia[i] > 0):
            array[j] = i
            copia[i] = copia[i] - 1
            j = j + 1

        main.event_generate("<<draw>>")
        if (stop[0]):
            return