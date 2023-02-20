from sorts.Algorithm import Algorithm

class CycleSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    
    def run(self):
        n = len(self._array)
        for i in range(0, n - 1):
            x = self._array[i]
            pos = i
            for j in range(i + 1, n):
                if self._array[j] < x:
                    pos += 1
                if(self._stop[0]):
                    return
            
            if pos == i:
                continue

            while x == self._array[pos]:
                pos += 1

            self._colors[pos] = self._sc
            self._array[pos], x = x, self._array[pos]
            self.drawSleep()
            self._colors[pos] = self._fc
            if(self._stop[0]):
                return

            while pos != i:
                pos = i
                for j in range(i + 1, n):
                    if self._array[j] < x:
                        pos += 1
                    if(self._stop[0]):
                        return

                while x == self._array[pos]:
                    pos += 1

                self._colors[pos] = self._sc
                self._array[pos], x = x, self._array[pos]
                self.drawSleep()
                self._colors[pos] = self._fc
                if(self._stop[0]):
                    return
        
    def info(self):
        pass