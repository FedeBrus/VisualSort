from sorts.Algorithm import Algorithm

class PancakeSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)

    def flip(self, k):
        left = 0
        while left < k:
            if(self._stop[0]):
                return
            self._colors[left] = self._sc
            self._colors[k] = self._sc
            self._array[left], self._array[k] = self._array[k], self._array[left]
            self.drawSleep()
            self._colors[left] = self._fc
            self._colors[k] = self._fc
            k -= 1
            left += 1

    def max_index(self, k):
        index = 0
        for i in range(k):
            if self._array[i] > self._array[index]:
                index = i
        return index

    def run(self):
        n = len(self._array)
        while n > 1:
            maxdex = self.max_index(n)
            self.flip(maxdex)
            self.flip(n - 1)
            n -= 1
            
    def info(self):
        pass