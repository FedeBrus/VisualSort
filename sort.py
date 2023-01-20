import time

def suck_cock():
    return

def bubble_sort(array, draw_array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if(array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_array(array)
                time.sleep(0.001)
    
def insertion_sort(array, draw_array):
    n = len(array)
    for i in range(1, n):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            draw_array(array)
            time.sleep(0.001)
            j -= 1

def selection_sort(array, draw_array):
    n = len(array)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if(array[j] < array[min_idx]):
                min_idx = j
        
        array[i], array[min_idx] = array[min_idx], array[i]
        draw_array(array)
        time.sleep(0.001)
        
