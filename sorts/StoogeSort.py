from sorts.Algorithm import Algorithm
import math

class StoogeSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    
    def run(self, start = -1, end = -1):
        if start == -1 and end == -1:
            start = 0
            end = len(self._array) - 1
        if(self._stop[0]):
            return
        if self._array[start] > self._array[end]:
            self._array[start], self._array[end] = self._array[end], self._array[start]
            self._colors[start] = self._sc
            self._colors[end] = self._sc
            self.drawSleep()
            self._colors[start] = self._fc
            self._colors[end] = self._fc

        length = end - start + 1
        if length >= 3:
            onethird = math.floor(length / 3)
            self.run(start, end - onethird)
            self.run(start + onethird, end)
            self.run(start, end - onethird)
    
    def info(self):
        pass