import time

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
            if(array[j] < array[min_idx]):
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
        time.sleep(0.001)
        

def merge_sort(array, main, stop, inf, sup):
    if inf < sup:
        ctr = (sup + inf) // 2
        merge_sort(array, main, stop, inf, ctr)
        merge_sort(array, main, stop, ctr + 1, sup)
        merge(array, main, stop, inf, ctr, sup)
