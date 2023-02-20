from sorts.Algorithm import Algorithm

class MergeSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    
    def merge(self, inf, ctr, sup):
        i, j, k = inf, ctr + 1, 0
        self._colors[inf] = self._sc
        self._colors[sup] = self._sc
        supp = [None] * (sup - inf + 1)
        while i <= ctr and j <= sup:
            if self._array[i] <= self._array[j]:
                supp[k] = self._array[i]
                i += 1
            else:
                supp[k] = self._array[j]
                j += 1
            k += 1

        while i <= ctr:
            supp[k] = self._array[i]
            k += 1
            i += 1

        while j <= sup:
            supp[k] = self._array[j]
            k += 1
            j += 1

        for i in range(sup - inf + 1):
            self._array[inf + i] = supp[i]
            self.drawSleep()
        
        self._colors[inf] = self._fc
        self._colors[sup] = self._fc
        
        if self._stop[0]:
            return
    
    def run(self, inf = -1, sup = -1):
        if inf == -1 and sup == -1:
            inf = 0
            sup = len(self._array) - 1
        
        if self._stop[0]:
            return
        
        if inf < sup:
            ctr = (sup + inf) // 2
            self.run(inf, ctr)
            if self._stop[0]:
                return
            self.run(ctr + 1, sup)
            if self._stop[0]:
                return
            self.merge(inf, ctr, sup)
        
    def info(self):
        pass