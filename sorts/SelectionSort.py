from sorts.Algorithm import Algorithm

class SelectionSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    
    def run(self):
        n = len(self._array)
        for i in range(0, n - 1):
            min_idx = i
            for j in range(i + 1, n):
                self._colors[j] = self._sc
                self.drawSleep()
                if self._stop[0]:
                    return
                if (self._array[j] < self._array[min_idx]):
                    self._colors[min_idx] = self._fc
                    min_idx = j
                    self._colors[min_idx] = self._tc
                if j != min_idx:
                    self._colors[j] = self._fc

            self._colors[min_idx] = self._fc
            self._array[i], self._array[min_idx] = self._array[min_idx], self._array[i]
            self.drawSleep()
            if self._stop[0]:
                return
        
    def info(self):
        pass