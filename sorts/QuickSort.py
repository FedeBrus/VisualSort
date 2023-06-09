from sorts.Algorithm import Algorithm

class QuickSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
        
    
    def partition(self, inf, sup):
        sample_size = 5
        if sup - inf + 1 >= sample_size:
            samples = [self._array[inf + i] for i in range(0, sample_size)]
            samples.sort
            self._array[sup], self._array[inf + sample_size // 2] = samples[sample_size // 2], self._array[sup] 
        
        x = self._array[sup]
        self._colors[sup] = self._sc
        i = inf - 1
        for j in range(inf, sup):
            if(self._array[j] <= x):
                i += 1
                self._array[i], self._array[j] = self._array[j], self._array[i]
                self.drawSleep()
            if (self._stop[0]):
                return i + 1

        self._colors[sup] = self._fc
        self._colors[i + 1] = self._tc
        self._array[i + 1], self._array[sup] = self._array[sup], self._array[i + 1]
        self.drawSleep()
        self._colors[i + 1] = self._fc
        return i + 1
        
    def run(self, inf = -1, sup = -1):
        if inf == -1 and sup == -1:
            inf = 0
            sup = len(self._array) - 1
        if (self._stop[0]):
            return
        if inf < sup:
            q = self.partition(inf, sup)
            self.run(inf, q - 1)
            self.run(q + 1, sup)
        self.reset_colors()
    
    def info(self):
        pass