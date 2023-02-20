from sorts.Algorithm import Algorithm
import math
from sort import othercolors

class IntroSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)

    def introinsertion(self, inf, sup):
        n = sup - inf + 1
        for i in range(1, n):
            j = i
            while j > 0 and self._array[inf + j - 1] > self._array[inf + j]:
                self._array[inf + j - 1], self._array[inf + j] = self._array[inf + j], self._array[inf + j - 1]
                j -= 1
                self._colors[inf + j] = self._sc
                self.drawSleep()
                self._colors[inf + j] = self._tc
                if self._stop[0]:
                    return
        return

    def introheapify(self, N, i, inf):
        if (self._stop[0]):
                return
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < N and self._array[inf + largest] < self._array[inf + l]:
            largest = l

        if r < N and self._array[inf + largest] < self._array[inf + r]:
            largest = r
            
        if largest != i:
            self._array[inf + i], self._array[inf + largest] = self._array[inf + largest], self._array[inf + i]  # swap
            self.introheapify(N, largest, inf)

    def introheap(self, inf, sup):
        N = sup - inf + 1

        for i in range(N//2 - 1, -1, -1):
            self.introheapify(N, i, inf)
            self.drawSleep()
            if (self._stop[0]):
                return

        bi = 0
        for i in range(math.ceil(math.log2(N))):
            for j in range(2**i):
                if(bi + j < N):
                    self._colors[inf + bi + j] = othercolors[i]
            bi = (bi << 1) + 1

        for i in range(N-1, 0, -1):
            self._array[inf + i], self._array[inf] = self._array[inf], self._array[inf + i]  # swap
            self.introheapify(i, 0, inf)
            self._colors[inf + i] = self._tc
            self.drawSleep()
            if (self._stop[0]):
                return
            
        self._colors[inf] = self._tc

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
    
    def introutil(self, maxdepth, inf, sup):
        n = sup - inf + 1
        #if n < 16:
        if n < 32:
            for i in range(inf, sup + 1):
                self._colors[i] = self._tc
            self.introinsertion(inf, sup)
            self.reset_colors()
        elif maxdepth == 0:
            for i in range(inf, sup + 1):
                self._colors[i] = self._tc
            self.introheap(inf, sup)
            self.reset_colors()
        else:
            q = self.partition(inf, sup)
            self.introutil(maxdepth - 1, inf, q - 1)
            self.introutil(maxdepth - 1, q + 1, sup)
        self.reset_colors()

    def run(self):
        maxdepth = 4
        #maxdepth = math.floor(math.log2(len(array))) * 2
        self.introutil(maxdepth, 0, len(self._array) - 1)
    
    def info(self):
        pass