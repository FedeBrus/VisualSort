from sorts.Algorithm import Algorithm

class CountingSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
        
    def run(self):
        maxA = (max(self._array) + 1)
        copia = [0] * maxA

        for i in range(len(self._array)):
            self._colors[i] = self._sc
            copia[self._array[i]] = copia[self._array[i]] + 1
            self.drawSleep()
            self._colors[i] = self._fc
            if (self._stop[0]):
                return

        j = 0
        for i in range(maxA):
            while (copia[i] > 0):
                self._array[j] = i
                copia[i] = copia[i] - 1
                j = j + 1

            self.drawSleep()
    
    def info(self):
        pass