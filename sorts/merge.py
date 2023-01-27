import time
import random
import threading
import math

def merge(array, main, stop, inf, ctr, sup):
    if stop[0]:
        return

    i, j, k = inf, ctr + 1, 0
    supp = [None] * (sup - inf + 1)
    while i <= ctr and j <= sup:
        if array[i] <= array[j]:
            supp[k] = array[i]
            i += 1
        else:
            supp[k] = array[j]
            j += 1
        k += 1
        if stop[0]:
            return

    while i <= ctr:
        supp[k] = array[i]
        k += 1
        i += 1
        if stop[0]:
            return

    while j <= sup:
        supp[k] = array[j]
        k += 1
        j += 1
        if stop[0]:
            return

    for i in range(sup - inf + 1):
        array[inf + i] = supp[i]
        main.event_generate("<<draw>>")
        time.sleep(0.001)


def merge_sort(array, main, stop, inf, sup):
    if inf < sup:
        ctr = (sup + inf) // 2
        merge_sort(array, main, stop, inf, ctr)
        merge_sort(array, main, stop, ctr + 1, sup)
        merge(array, main, stop, inf, ctr, sup)