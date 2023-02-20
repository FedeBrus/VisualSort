from sorts.Algorithm import Algorithm
import time
import threading

class SleepSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
        
    def run(self):
        copia = self._array.copy()
        self._array.clear()
        
        e = threading.Event()

        def s_sort(val):
            e.wait((0.1 * val) * (0.001 * 1000))
            self._array.append(val)
            self._main.event_generate("<<draw>>")

        for x in copia:
            threading.Thread(target=s_sort, args=[x]).start()
        
        copia = sorted(copia)
        uscita = False
        while self._array != copia and uscita == False:
            if self._stop[0]:
                e.set()
                uscita = True
            time.sleep(0.5)
        
    def info(self):
        pass