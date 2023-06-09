from sorts.Algorithm import Algorithm

class Radix2LSDSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    
    def run(self):
        n = len(self._array)
        max_cifre = max(self._array)
        posto = 1
        while max_cifre // posto > 0:
            output = [0] * n
            count = [0] * 2

            for i in range(0, n):
                index = self._array[i] // posto
                count[index % 2] += 1

            for i in range(1, 2):
                count[i] += count[i - 1]
                
            i = n - 1
            while i >= 0:
                index = self._array[i] // posto
                output[count[index % 2] - 1] = self._array[i]
                count[index % 2] -= 1
                i -= 1
                if (self._stop[0]):
                    return

            for i in range(0, n):
                self._array[i] = output[i]
                self._colors[i] = self._sc
                self.drawSleep()
                self._colors[i] = self._fc
                if (self._stop[0]):
                    return
                
            if (self._stop[0]):
                return
                
            posto *= 2
            self.drawSleep()
    
    def info(self):
        pass