from sorts.Algorithm import Algorithm
import random

class BogoSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    
    def run(self):
        while self._array != sorted(self._array):
            x = random.randint(0, len(self._array) - 1)
            y = random.randint(0, len(self._array) - 1)
            self._colors[x] = self._sc
            self._colors[y] = self._sc
            self.drawSleep()
            self._array[x], self._array[y] = self._array[y], self._array[x]
            self._colors[x] = self._fc
            self._colors[y] = self._fc

        if (self._stop[0]):
            return
        
    def info(self):
        pass