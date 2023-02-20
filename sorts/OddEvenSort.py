from sorts.Algorithm import Algorithm

class OddEvenSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    
    def run(self):
        n = len(self._array)
        sorted = False
        while not sorted:
            sorted = True
            for i in range(1, n - 1, 2):
                if self._array[i] > self._array[i + 1]:
                    self._colors[i] = self._sc
                    self._colors[i + 1] = self._sc
                    self._array[i], self._array[i + 1] = self._array[i + 1], self._array[i]
                    self.drawSleep()
                    self._colors[i] = self._fc
                    self._colors[i + 1] =self._fc
                    sorted = False
                    if self._stop[0]:
                        return
            for i in range(0, n - 1, 2):
                if self._array[i] > self._array[i + 1]:
                    self._colors[i] = self._sc
                    self._colors[i + 1] = self._sc
                    self._array[i], self._array[i + 1] = self._array[i + 1], self._array[i]
                    self.drawSleep()
                    self._colors[i] = self._fc
                    self._colors[i + 1] = self._fc
                    sorted = False
                    if self._stop[0]:
                        return
        self.reset_colors()    
    def info(self):
        pass
    