from sorts.Algorithm import Algorithm

class GnomeSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    
    
    def run(self):
        n = len(self._array)
        pos = 0
        while(pos < n):
            if(pos == 0 or self._array[pos] >= self._array[pos - 1]):
                pos += 1
                if pos < n:
                    self._colors[pos] = self._sc 
                self.drawSleep()
            else:
                self._array[pos], self._array[pos - 1] = self._array[pos - 1], self._array[pos]
                pos -= 1
                if pos >= 0:
                    self._colors[pos] = self._sc
                self.drawSleep()
            if pos >= 0 and pos < n:
                self._colors[pos] = self._fc
            if(self._stop[0]):
                return
            
    def info(self):
        pass