from sorts.Algorithm import Algorithm

class BubbleSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    
    def run(self):
        n = len(self._array)
        sorted = False
        i = 0
        while not sorted and i < n:
            sorted = True
            for j in range(n - i - 1):
                if self._array[j] > self._array[j + 1]:
                    self._array[j], self._array[j + 1] = self._array[j + 1], self._array[j]
                    sorted = False
                    self._colors[j + 1] = self._sc
                    self.drawSleep()
                    self._colors[j + 1] = self._fc
                if self._stop[0]:
                    return
            i += 1
        
    def info(self):
        pass