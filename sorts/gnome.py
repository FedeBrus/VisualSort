import time
import random
import threading
import math

def gnome_sort(array, main, stop):
    # Per ora identico all'insertion sort, quando faremo anche i colori si noterà la differenza
    n = len(array)
    pos = 0
    while(pos < n):
        if(pos == 0 or array[pos] >= array[pos - 1]):
            pos += 1
        else:
            array[pos], array[pos - 1] = array[pos - 1], array[pos]
            pos -= 1
            main.event_generate("<<draw>>")
            time.sleep(0.001)
        
        if(stop[0]):
            return