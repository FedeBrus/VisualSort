from sorts.Algorithm import Algorithm

class ShellSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
        
    def run(self):
        n = len(self._array)
        gaps = [701, 301, 132, 57, 23, 10, 4, 1]
        for gap in gaps:
            for i in range(gap, n):
                self._colors[i] = self._tc
                if self._stop[0]:
                    return
                self.drawSleep()
                tmp = self._array[i]
                j = i
                while j >= gap and self._array[j - gap] > tmp:
                    if self._stop[0]:
                        return
                    self._array[j] = self._array[j - gap]
                    if j != i:
                        self._colors[j + gap] = self._sc
                    self._colors[j] = self._tc
                    self._colors[j - gap] = self._sc
                    j -= gap
                    self.drawSleep()
                self._array[j] = tmp
                self.reset_colors()
                if j != i:
                    if self._stop[0]:
                        return
                    self._colors[j] = self._tc
                    self.drawSleep()
                    self.reset_colors()
        self.reset_colors()
    
    def info(self):
        pass