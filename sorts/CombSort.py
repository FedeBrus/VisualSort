from sorts.Algorithm import Algorithm
import math

class CombSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
        
    
    def run(self):
        n = len(self._array)
        shrink = 1.33
        gap = n
        sorted = False
        while not sorted:
            sorted = True
            gap = math.floor(gap / shrink)
            if gap < 1:
                gap = 1
            for i in range(0, n - gap):
                if self._array[i] > self._array[i + gap]:
                    self._colors[i] = self._sc
                    self._colors[i + gap] = self._sc
                    self._array[i], self._array[i + gap] = self._array[i + gap], self._array[i]
                    self.drawSleep()
                    self._colors[i] = self._fc
                    self._colors[i + gap] = self._fc
                    if(self._stop[0]):
                        return
                    sorted = False
        self.reset_colors()
        
    def info(self):
        pass