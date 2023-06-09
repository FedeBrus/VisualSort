from sorts.Algorithm import Algorithm

class CocktailSorterSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
        
    def run(self):
        n = len(self._array)
        i = 0
        j = n - 1
        sorted = False
        while not sorted:
            sorted = True
            for idx in range(i, j):
                if(self._array[idx] > self._array[idx + 1]):
                    self._colors[idx + 1] = self._sc
                    self._array[idx], self._array[idx + 1] = self._array[idx + 1], self._array[idx]
                    self.drawSleep()
                    self._colors[idx + 1] = self._fc
                    if(self._stop[0]):
                        return
                    sorted = False

            j -= 1
            if sorted:
                self.reset_colors()
                return
            else:
                for idx in range(j, i - 1, -1):
                    if(self._array[idx] > self._array[idx + 1]):
                        self._colors[idx] = self._sc
                        self._array[idx], self._array[idx + 1] = self._array[idx + 1], self._array[idx]
                        self.drawSleep()
                        self._colors[idx] = self._fc
                        if(self._stop[0]):
                            return
                        sorted = False
                i += 1
        self.reset_colors()
    
    def info(self):
        pass