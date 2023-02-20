from sorts.Algorithm import Algorithm
import math

class BucketSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)

    def bucketinsertion(self, inf, sup):
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
    

    def run(self):
        n = len(self._array)
        m = max(self._array) + 1
        k = n // 20 if n >= 20 else 1
        buckets = [[] for i in range(0, k)]
        
        for i in range(0, n):
            buckets[math.floor(k * self._array[i] / m)].append(self._array[i])
        
        idx = 0
        for i in range(0, k):
            for j in range(0, len(buckets[i])):
                self._array[idx] = buckets[i][j]
                self.drawSleep()
                if(self._stop[0]):
                    return
                idx += 1

        idx = 0
        for i in range(0, k):
            for j in range(len(buckets[i])):
                self._colors[idx + j] = self._tc
            self.bucketinsertion(idx, idx + len(buckets[i]) - 1)
            self.reset_colors()
            idx += len(buckets[i])

        self.reset_colors()
    
    def info(self):
        pass