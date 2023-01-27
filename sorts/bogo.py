import time
import random
import threading
import math

def bogo_sort(array, main, stop):
    while array != sorted(array):
        x = random.randint(0, len(array) - 1)
        y = random.randint(0, len(array) - 1)
        array[x], array[y] = array[y], array[x]
        main.event_generate("<<draw>>")
        if (stop[0]):
            return