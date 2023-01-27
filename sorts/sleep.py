import time
import random
import threading
import math

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