import time
import random
import threading
import math

def radix_sort(array, main, stop):
    max_cifre = max(array)
    posto = 1
    while max_cifre // posto > 0:
        size = len(array)
        output = [0] * size
        count = [0] * 10

        for i in range(0, size):
            index = array[i] // posto
            count[index % 10] += 1


        for i in range(1, 10):
            count[i] += count[i - 1]

            
        i = size - 1
        while i >= 0:
            index = array[i] // posto
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1
            if (stop[0]):
                return

            
        for i in range(0, size):
            array[i] = output[i]
            main.event_generate("<<draw>>")
            if (stop[0]):
                return
            
        if (stop[0]):
            return
            
        posto *= 10
        main.event_generate("<<draw>>")