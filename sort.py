import time
import random
import threading
import math

global velocity
velocity = [0.0]

fc = '#cc241d'
sc = '#ebdbb2'
tc = '#b8bb26'
othercolors = ["#928374", "#fabd2f", "#83a598", "#d3869b", "#fe8019", '#8ec07c', '#f92672', '#7fffd4', '#e1c699', '#c8a2c8']

def reset_colors(array, colors, main):
    n = len(array)
    for i in range(n):
        colors[i] = fc
    main.event_generate("<<draw>>")

def bubble_sort(array, main, stop, colors):
    n = len(array)
    sorted = False
    i = 0
    while not sorted and i < n:
        sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted = False
                colors[j + 1] = sc
                time.sleep(velocity[0])
                main.event_generate("<<draw>>")
                colors[j + 1] = fc
            if stop[0]:
                return
        i += 1


def insertion_sort(array, main, stop, colors):
    n = len(array)
    for i in range(1, n):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
            colors[j] = sc
            time.sleep(velocity[0])
            main.event_generate("<<draw>>")
            colors[j] = fc
            if stop[0]:
                return
    

def selection_sort(array, main, stop, colors):
    n = len(array)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            colors[j] = sc
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
            if stop[0]:
                return
            if (array[j] < array[min_idx]):
                colors[min_idx] = fc
                min_idx = j
                colors[min_idx] = tc
            if j != min_idx:
                colors[j] = fc

        colors[min_idx] = fc
        array[i], array[min_idx] = array[min_idx], array[i]
        main.event_generate("<<draw>>")
        time.sleep(velocity[0])
        if stop[0]:
            return
    

def merge(array, main, stop, inf, ctr, sup, colors):
    i, j, k = inf, ctr + 1, 0
    colors[inf] = sc
    colors[sup] = sc
    supp = [None] * (sup - inf + 1)
    while i <= ctr and j <= sup:
        if array[i] <= array[j]:
            supp[k] = array[i]
            i += 1
        else:
            supp[k] = array[j]
            j += 1
        k += 1

    while i <= ctr:
        supp[k] = array[i]
        k += 1
        i += 1

    while j <= sup:
        supp[k] = array[j]
        k += 1
        j += 1

    for i in range(sup - inf + 1):
        array[inf + i] = supp[i]
        main.event_generate("<<draw>>")
        time.sleep(velocity[0])
        if stop[0]:
            return

    colors[inf] = fc
    colors[sup] = fc

def merge_sort(array, main, stop, inf, sup, colors):
    if inf < sup:
        ctr = (sup + inf) // 2
        merge_sort(array, main, stop, inf, ctr, colors)
        merge_sort(array, main, stop, ctr + 1, sup, colors)
        merge(array, main, stop, inf, ctr, sup, colors)


def counting_sort(array, main, stop, colors):
    maxA = (max(array) + 1)
    copia = [0] * maxA

    for i in range(len(array)):
        colors[i] = sc
        copia[array[i]] = copia[array[i]] + 1
        main.event_generate("<<draw>>")
        time.sleep(velocity[0])
        colors[i] = fc
        if (stop[0]):
            return

    j = 0
    for i in range(maxA):
        while (copia[i] > 0):
            array[j] = i
            copia[i] = copia[i] - 1
            j = j + 1

        main.event_generate("<<draw>>")
        time.sleep(velocity[0])
        if (stop[0]):
            return


def bogo_sort(array, main, stop, colors):
    while array != sorted(array):
        x = random.randint(0, len(array) - 1)
        y = random.randint(0, len(array) - 1)
        colors[x] = sc
        colors[y] = sc
        main.event_generate("<<draw>>")
        array[x], array[y] = array[y], array[x]
        colors[x] = fc
        colors[y] = fc
        time.sleep(velocity[0])
        if (stop[0]):
            return

def heapify(arr, N, i, stop, colors):
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
        heapify(arr, N, largest, stop, colors)

def heap_sort(array, main, stop, colors):

    N = len(array)

    for i in range(N // 2 - 1, -1, -1):
        heapify(array, N, i, stop, colors)
        main.event_generate("<<draw>>")
        time.sleep(velocity[0])
        if (stop[0]):
            return
    bi = 0
    for i in range(math.ceil(math.log2(N))):
        for j in range(2**i):
            if(bi + j < N):
                colors[bi + j] = othercolors[i]
        bi = (bi << 1) + 1

    for i in range(N-1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        heapify(array, i, 0, stop, colors)
        colors[i] = fc
        main.event_generate("<<draw>>")
        time.sleep(velocity[0])
        if (stop[0]):
            return
    
    colors[0] = fc

def radix10LSD_sort(array, main, stop, colors):
    n = len(array)
    max_cifre = max(array)
    posto = 1
    while max_cifre // posto > 0:
        output = [0] * n
        count = [0] * 10

        for i in range(0, n):
            index = array[i] // posto
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]
            
        i = n - 1
        while i >= 0:
            index = array[i] // posto
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1
            if (stop[0]):
                return

        for i in range(0, n):
            array[i] = output[i]
            colors[i] = sc
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
            colors[i] = fc
            if (stop[0]):
                return
            
        if (stop[0]):
            return
            
        posto *= 10

        main.event_generate("<<draw>>")
        time.sleep(velocity[0])

def radix2LSD_sort(array, main, stop, colors):
    n = len(array)
    max_cifre = max(array)
    posto = 1
    while max_cifre // posto > 0:
        output = [0] * n
        count = [0] * 2

        for i in range(0, n):
            index = array[i] // posto
            count[index % 2] += 1

        for i in range(1, 2):
            count[i] += count[i - 1]
            
        i = n - 1
        while i >= 0:
            index = array[i] // posto
            output[count[index % 2] - 1] = array[i]
            count[index % 2] -= 1
            i -= 1
            if (stop[0]):
                return

        for i in range(0, n):
            array[i] = output[i]
            colors[i] = sc
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
            colors[i] = fc
            if (stop[0]):
                return
            
        if (stop[0]):
            return
            
        posto *= 2
        main.event_generate("<<draw>>")
        time.sleep(velocity[0])

def partition(array, main, stop, inf, sup, colors):
    # Questo campionamento serve a prende un pivot abbastanza bilanciato, per migliorare l'effetto visivo
    sample_size = 5
    if sup - inf + 1 >= sample_size:
        samples = [array[inf + i] for i in range(0, sample_size)]
        samples.sort
        array[sup], array[inf + sample_size // 2] = samples[sample_size // 2], array[sup] 
    
    x = array[sup]
    colors[sup] = sc
    i = inf - 1
    for j in range(inf, sup):
        if(array[j] <= x):
            i += 1
            array[i], array[j] = array[j], array[i]
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
        if (stop[0]):
            return i + 1

    colors[sup] = fc
    array[i + 1], array[sup] = array[sup], array[i + 1]
    main.event_generate("<<draw>>")
    time.sleep(velocity[0])
    return i + 1
    
def quick_sort(array, main, stop, inf, sup, colors):
    if (stop[0]):
        return
    if inf < sup:
        q = partition(array, main, stop, inf, sup, colors)
        quick_sort(array, main, stop, inf, q - 1, colors)
        quick_sort(array, main, stop, q + 1, sup, colors)
    reset_colors(array, colors, main)

def gnome_sort(array, main, stop, colors):
    n = len(array)
    pos = 0
    while(pos < n):
        if(pos == 0 or array[pos] >= array[pos - 1]):
            pos += 1
            if pos < n:
                colors[pos] = sc 
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
        else:
            array[pos], array[pos - 1] = array[pos - 1], array[pos]
            pos -= 1
            if pos >= 0:
                colors[pos] = sc
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
        if pos >= 0 and pos < n:
            colors[pos] = fc
        if(stop[0]):
            return
    

def introinsertion(array, main, stop, inf, sup, colors):
    n = sup - inf + 1
    for i in range(1, n):
        j = i
        while j > 0 and array[inf + j - 1] > array[inf + j]:
            array[inf + j - 1], array[inf + j] = array[inf + j], array[inf + j - 1]
            j -= 1
            colors[inf + j] = sc
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
            colors[inf + j] = tc
            if stop[0]:
                return
    return

def introheapify(arr, N, i, stop, inf, colors):
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
        introheapify(arr, N, largest, stop, inf, colors)

def introheap(array, main, stop, inf, sup, colors):
    N = sup - inf + 1

    for i in range(N//2 - 1, -1, -1):
        introheapify(array, N, i, stop, inf, colors)
        main.event_generate("<<draw>>")
        time.sleep(velocity[0])
        if (stop[0]):
            return

    bi = 0
    for i in range(math.ceil(math.log2(N))):
        for j in range(2**i):
            if(bi + j < N):
                colors[inf + bi + j] = othercolors[i]
        bi = (bi << 1) + 1

    for i in range(N-1, 0, -1):
        array[inf + i], array[inf] = array[inf], array[inf + i]  # swap
        introheapify(array, i, 0, stop, inf, colors)
        colors[inf + i] = tc
        main.event_generate("<<draw>>")
        time.sleep(velocity[0])
        if (stop[0]):
            return
        
    colors[inf] = tc

def introutil(array, main, stop, maxdepth, inf, sup, colors):
    n = sup - inf + 1
    #if n < 16:
    if n < 32:
        for i in range(inf, sup + 1):
            colors[i] = tc
        introinsertion(array, main, stop, inf, sup, colors)
        reset_colors(array, colors, main)
    elif maxdepth == 0:
        for i in range(inf, sup + 1):
            colors[i] = tc
        introheap(array, main, stop, inf, sup, colors)
        reset_colors(array, colors, main)
    else:
        q = partition(array, main, stop, inf, sup, colors)
        introutil(array, main, stop, maxdepth - 1, inf, q - 1, colors)
        introutil(array, main, stop, maxdepth - 1, q + 1, sup, colors)
    reset_colors(array, colors, main)

def intro_sort(array, main, stop, colors):
    maxdepth = 4
    #maxdepth = math.floor(math.log2(len(array))) * 2
    introutil(array, main, stop, maxdepth, 0, len(array) - 1, colors)

def sleep_sort(array: list, main, stop):
    copia = array.copy()
    array.clear()
    
    e = threading.Event()

    def s_sort(val):
        e.wait((0.1 * val) + (velocity[0] * 1000))
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

def shell_sort(array, main, stop, colors):
    n = len(array)
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, n):
            colors[i] = tc
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
            tmp = array[i]
            j = i
            while j >= gap and array[j - gap] > tmp:
                array[j] = array[j - gap]
                if j != i:
                    colors[j + gap] = sc
                colors[j] = tc
                colors[j - gap] = sc
                j -= gap
                main.event_generate("<<draw>>")
                time.sleep(velocity[0])
                if stop[0]:
                    return
            array[j] = tmp
            reset_colors(array, colors, main)
            if j != i:
                colors[j] = tc
                main.event_generate("<<draw>>")
                time.sleep(velocity[0])
                reset_colors(array, colors, main)
    reset_colors(array, colors, main)

def oddeven_sort(array, main, stop, colors):
    n = len(array)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, n - 1, 2):
            if array[i] > array[i + 1]:
                colors[i] = sc
                colors[i + 1] = sc
                array[i], array[i + 1] = array[i + 1], array[i]
                main.event_generate("<<draw>>")
                time.sleep(velocity[0])
                colors[i] = fc
                colors[i + 1] = fc
                sorted = False
                if stop[0]:
                    return
        for i in range(0, n - 1, 2):
            if array[i] > array[i + 1]:
                colors[i] = sc
                colors[i + 1] = sc
                array[i], array[i + 1] = array[i + 1], array[i]
                main.event_generate("<<draw>>")
                time.sleep(velocity[0])
                colors[i] = fc
                colors[i + 1] = fc
                sorted = False
                if stop[0]:
                    return
    reset_colors(array, colors, main)

def bucketinsertion(array, main, stop, inf, sup, colors):
    n = sup - inf + 1
    for i in range(1, n):
        j = i
        while j > 0 and array[inf + j - 1] > array[inf + j]:
            array[inf + j - 1], array[inf + j] = array[inf + j], array[inf + j - 1]
            j -= 1
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
            if stop[0]:
                return
    return

def bucket_sort(array, main, stop, colors):
    n = len(array)
    m = max(array) + 1
    k = n // 20 if n >= 20 else 1
    buckets = [[] for i in range(0, k)]
    
    for i in range(0, n):
        buckets[math.floor(k * array[i] / m)].append(array[i])
    
    idx = 0
    for i in range(0, k):
        for j in range(0, len(buckets[i])):
            array[idx] = buckets[i][j]
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
            if(stop[0]):
                return
            idx += 1

    idx = 0
    for i in range(0, k):
        for j in range(len(buckets[i])):
            colors[idx + j] = tc
        bucketinsertion(array, main, stop, idx, idx + len(buckets[i]) - 1, colors)
        reset_colors(array, colors, main)
        idx += len(buckets[i])

    reset_colors(array, colors, main)

def cocktailshaker_sort(array, main, stop, colors):
    n = len(array)
    i = 0
    j = n - 1
    sorted = False
    while not sorted:
        sorted = True
        for idx in range(i, j):
            if(array[idx] > array[idx + 1]):
                colors[idx + 1] = sc
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
                main.event_generate("<<draw>>")
                time.sleep(velocity[0])
                colors[idx + 1] = fc
                if(stop[0]):
                    return
                sorted = False

        j -= 1
        if sorted:
            reset_colors(array, colors, main)
            return
        else:
            for idx in range(j, i - 1, -1):
                if(array[idx] > array[idx + 1]):
                    colors[idx] = sc
                    array[idx], array[idx + 1] = array[idx + 1], array[idx]
                    main.event_generate("<<draw>>")
                    time.sleep(velocity[0])
                    colors[idx] = fc
                    if(stop[0]):
                        return
                    sorted = False
            i += 1
    reset_colors(array, colors, main)

def comb_sort(array, main, stop, colors):
    n = len(array)
    shrink = 1.33
    gap = n
    sorted = False
    while not sorted:
        sorted = True
        gap = math.floor(gap / shrink)
        if gap < 1:
            gap = 1
        for i in range(0, n - gap):
            if array[i] > array[i + gap]:
                colors[i] = sc
                colors[i + gap] = sc
                array[i], array[i + gap] = array[i + gap], array[i]
                main.event_generate("<<draw>>")
                time.sleep(velocity[0])
                colors[i] = fc
                colors[i + gap] = fc
                if(stop[0]):
                    return
                sorted = False
    reset_colors(array, colors, main)

class BST:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def insert(self, val):
        if self.value == None:
            self.value = val
        else:
            if val < self.value:
                if self.left == None:
                    self.left = BST()
                self.left.insert(val)
            else:
                if self.right == None:
                    self.right = BST()
                self.right.insert(val)

    def ascending(self, array, main, stop):
        if self.value != None:
            if self.left == None:
                self.left = BST()
            self.left.ascending(array, main, stop)
            
            array.append(self.value)
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
            if(stop[0]):
                return
            
            if self.right == None:
                self.right = BST()
            self.right.ascending(array, main, stop)

def tree_sort(array, main, stop):
    tree = BST()
    i = 0
    n = len(array)
    while i < n:
        tree.insert(array.pop(0))
        main.event_generate("<<draw>>")
        time.sleep(velocity[0]) 
        if(stop[0]):
            return
        i += 1

    tree.ascending(array, main, stop)
    
def strand_sort(array: list, superlist, ric, main, stop, colors):
    if(len(superlist) == 0):
        return
    else:
        if(ric[0] == 0):
            superlist = array.copy()
            array.clear()
        sublist = []
        sublist.append(superlist.pop(0))
        i = 0
        idx = 0
        while i < len(superlist):
            if(superlist[i] > sublist[idx]):
                sublist.append(superlist.pop(i))
                i -= 1
                idx += 1
            i += 1

        if ric[0] == 0:
            i = 0
            while i < len(sublist):
                array.append(sublist[i])
                main.event_generate("<<draw>>")
                time.sleep(velocity[0])
                if(stop[0]):
                    return
                i += 1
        else:
            subend = len(sublist) - 1
            solstart = 0;
            while len(sublist) > 0:
                if sublist[subend] > array[solstart]:
                    solstart += 1
                else:
                    array.insert(solstart, sublist.pop(subend))
                    main.event_generate("<<draw>>")
                    time.sleep(velocity[0])
                    if(stop[0]):
                        return
                    subend -= 1
                    solstart = 0
        
        ric[0] += 1
        time.sleep(velocity[0] * 2)
        strand_sort(array, superlist, ric, main, stop, colors)

def cycle_sort(array, main, stop, colors):
    n = len(array)
    for i in range(0, n - 1):
        x = array[i]
        pos = i
        for j in range(i + 1, n):
            if array[j] < x:
                pos += 1
            if(stop[0]):
                return
        
        if pos == i:
            continue

        while x == array[pos]:
            pos += 1

        colors[pos] = sc
        array[pos], x = x, array[pos]
        main.event_generate("<<draw>>")
        time.sleep(velocity[0])
        colors[pos] = fc
        if(stop[0]):
            return

        while pos != i:
            pos = i
            for j in range(i + 1, n):
                if array[j] < x:
                    pos += 1
                if(stop[0]):
                    return

            while x == array[pos]:
                pos += 1

            colors[pos] = sc
            array[pos], x = x, array[pos]
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
            colors[pos] = fc
            if(stop[0]):
                return

def stooge_sort(array, main, stop, start, end, colors):
    if(stop[0]):
        return
    if array[start] > array[end]:
        array[start], array[end] = array[end], array[start]
        colors[start] = sc
        colors[end] = sc
        main.event_generate("<<draw>>")
        colors[start] = fc
        colors[end] = fc
        time.sleep(velocity[0])
    
    length = end - start + 1
    if length >= 3:
        onethird = math.floor(length / 3)
        stooge_sort(array, main, stop, start, end - onethird, colors)
        stooge_sort(array, main, stop, start + onethird, end, colors)
        stooge_sort(array, main, stop, start, end - onethird, colors)
            
def flip(array, main, stop, k, colors):
    left = 0
    while left < k:
        if(stop[0]):
            return
        colors[left] = sc
        colors[k] = sc
        array[left], array[k] = array[k], array[left]
        main.event_generate("<<draw>>")
        time.sleep(velocity[0])
        colors[left] = fc
        colors[k] = fc
        k -= 1
        left += 1

def max_index(array, k):
    index = 0
    for i in range(k):
        if array[i] > array[index]:
            index = i
    return index

def pancake_sort(array, main, stop, colors):
    n = len(array)
    while n > 1:
        maxdex = max_index(array, n)
        flip(array, main, stop, maxdex, colors)
        flip(array, main, stop, n - 1, colors)
        n -= 1
    
def slow_sort(array, main, stop, colors, start, end):
    if start >= end or stop[0]:
        return
    
    middle = math.floor((start + end) / 2);
    slow_sort(array, main, stop, colors, start, middle);
    slow_sort(array, main, stop, colors, middle + 1, end);
    
    if array[end] < array[middle]:
        array[end], array[middle] = array[middle], array[end]
        
    time.sleep(velocity[0])
    slow_sort(array, main, stop, colors, start, end - 1)
    colors[end] = sc
    colors[start] = sc
    main.event_generate("<<draw>>")
    colors[end] = fc
    colors[start] = fc