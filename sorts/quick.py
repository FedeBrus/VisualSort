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
    
def quick_sort(array, main, stop, inf, sup):
    if (stop[0]):
        return
    if inf < sup:
        q = partition(array, main, stop, inf, sup)
        quick_sort(array, main, stop, inf, q - 1)
        quick_sort(array, main, stop, q + 1, sup)