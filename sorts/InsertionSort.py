from sorts.Algorithm import Algorithm

class InsertionSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    
    def run(self):
        n = len(self._array)
        for i in range(1, n):
            j = i
            while j > 0 and self._array[j - 1] > self._array[j]:
                self._array[j - 1], self._array[j] = self._array[j], self._array[j - 1]
                j -= 1
                self._colors[j] = self._sc
                self.drawSleep()
                self._colors[j] = self._fc
                if self._stop[0]:
                    return
    
    def info(self):
        pass