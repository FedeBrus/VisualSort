from sorts.Algorithm import Algorithm
import math

class SlowSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
        
    def run(self, start = -1, end = -1):
        if start == -1 and end == -1:
            start = 0
            end = len(self._array) - 1
        if start >= end or self._stop[0]:
            return
        
        middle = math.floor((start + end) / 2);
        self.run(start, middle);
        self.run(middle + 1, end);
        
        if self._array[end] < self._array[middle]:
            self._array[end], self._array[middle] = self._array[middle], self._array[end]
            
        self.run(start, end - 1)
        self._colors[end] = self._sc
        self._colors[start] = self._sc
        if self._stop[0]:
            return
        self.drawSleep()
        self._colors[end] = self._fc
        self._colors[start] = self._fc
        
    def info(self):
        pass