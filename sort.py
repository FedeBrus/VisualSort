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


def bogo_sort(array, main, stop):
    while array != sorted(array):
        x = random.randint(0, len(array) - 1)
        y = random.randint(0, len(array) - 1)
        array[x], array[y] = array[y], array[x]
        main.event_generate("<<draw>>")
        if (stop[0]):
            return


def heapify(arr, N, i, stop):
    if (stop[0]):
            return
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, N, largest, stop)


def heap_sort(array, main, stop):

    N = len(array)

    for i in range(N//2 - 1, -1, -1):
        heapify(array, N, i, stop)
        main.event_generate("<<draw>>")
        if (stop[0]):
            return

    for i in range(N-1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        heapify(array, i, 0, stop)
        main.event_generate("<<draw>>")
        if (stop[0]):
            return

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
    
def quick_sort(array, main, stop, inf, sup):
    if (stop[0]):
        return
    if inf < sup:
        q = partition(array, main, stop, inf, sup)
        quick_sort(array, main, stop, inf, q - 1)
        quick_sort(array, main, stop, q + 1, sup)

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

def sleep_sort(array: list, main, stop):
    copia = array.copy()
    array.clear()
    
    e = threading.Event()

    def s_sort(val):
        e.wait(0.1 * val)
        array.append(val)
        main.event_generate("<<draw>>")

    for x in copia:
        threading.Thread(target=s_sort, args=[x]).start()
    
    copia = sorted(copia)
    uscita = False
    while array != copia and uscita == False:
        if stop[0]:
            e.set()
            uscita = True
        time.sleep(0.5)

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