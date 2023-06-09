from sorts.Algorithm import Algorithm
import math

class HeapSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
        from sort import othercolors
        self._othercolors =  othercolors
    
    
    def heapify(self, N, i):
        if (self._stop[0]):
            return
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < N and self._array[largest] < self._array[l]:
            largest = l

        if r < N and self._array[largest] < self._array[r]:
            largest = r
            
        if largest != i:
            self._array[i], self._array[largest] = self._array[largest], self._array[i]  # swap
            self.heapify(N, largest)

        
    def run(self):
        N = len(self._array)

        for i in range(N // 2 - 1, -1, -1):
            self.heapify(N, i)
            self.drawSleep()
            if (self._stop[0]):
                return
        bi = 0
        for i in range(math.ceil(math.log2(N))):
            for j in range(2**i):
                if(bi + j < N):
                    self._colors[bi + j] = self._othercolors[i]
            bi = (bi << 1) + 1

        for i in range(N-1, 0, -1):
            self._array[i], self._array[0] = self._array[0], self._array[i]  # swap
            self.heapify(i, 0)
            self._colors[i] = self._fc
            self.drawSleep()
            if (self._stop[0]):
                return
        
        self._colors[0] = self._fc
    
    def info(self):
        pass