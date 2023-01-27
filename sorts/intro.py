import time
import random
import threading
import math

def partition(array, main, stop, inf, sup):
    # Questo campionamento serve a prende un pivot abbastanza bilanciato, per migliorare l'effetto visivo
    sample_size = 5
    if sup - inf + 1 >= sample_size:
        samples = [array[inf + i] for i in range(0, sample_size)]
        samples.sort
        array[sup], array[inf + sample_size // 2] = samples[sample_size // 2], array[sup] 
    
    x = array[sup]
    i = inf - 1
    for j in range(inf, sup):
        if(array[j] <= x):
            i += 1
            array[i], array[j] = array[j], array[i]
            main.event_generate("<<draw>>")
            time.sleep(0.001)
        if (stop[0]):
            return i + 1

    array[i + 1], array[sup] = array[sup], array[i + 1]
    main.event_generate("<<draw>>")
    time.sleep(0.001)
    return i + 1

def introinsertion(array, main, stop, inf, sup):
    n = sup - inf + 1
    for i in range(1, n):
        j = i
        while j > 0 and array[inf + j - 1] > array[inf + j]:
            array[inf + j - 1], array[inf + j] = array[inf + j], array[inf + j - 1]
            j -= 1
            main.event_generate("<<draw>>")
            time.sleep(0.001)
            if stop[0]:
                return
    return

def introheapify(arr, N, i, stop, inf):
    if (stop[0]):
            return
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[inf + largest] < arr[inf + l]:
        largest = l

    if r < N and arr[inf + largest] < arr[inf + r]:
        largest = r
        
    if largest != i:
        arr[inf + i], arr[inf + largest] = arr[inf + largest], arr[inf + i]  # swap
        introheapify(arr, N, largest, stop, inf)

def introheap(array, main, stop, inf, sup):
    N = sup - inf + 1

    for i in range(N//2 - 1, -1, -1):
        introheapify(array, N, i, stop, inf)
        main.event_generate("<<draw>>")
        if (stop[0]):
            return

    for i in range(N-1, 0, -1):
        array[inf + i], array[inf] = array[inf], array[inf + i]  # swap
        introheapify(array, i, 0, stop, inf)
        main.event_generate("<<draw>>")
        if (stop[0]):
            return

def introutil(array, main, stop, maxdepth, inf, sup):
    n = sup - inf + 1
    #if n < 16:
    if n < 64:
        introinsertion(array, main, stop, inf, sup)
    elif maxdepth == 0:
        introheap(array, main, stop, inf, sup)
    else:
        q = partition(array, main, stop, inf, sup)
        introutil(array, main, stop, maxdepth - 1, inf, q - 1)
        introutil(array, main, stop, maxdepth - 1, q + 1, sup)

def intro_sort(array, main, stop):
    maxdepth = 3
    #maxdepth = math.floor(math.log2(len(array))) * 2
    introutil(array, main, stop, maxdepth, 0, len(array) - 1)