from time import sleep
import abc

class Algorithm(abc.ABC):
    def __init__(self, array, main, stop, colors) -> None:
        from sort import fc, sc, tc, velocity
        self._array = array
        self._main = main
        self._stop = stop
        self._colors = colors
        self._fc = fc
        self._sc = sc
        self._tc = tc
        self._velocity = velocity
    
    @classmethod
    def fromAlgorithm(cls, algo):
        return cls(algo._array, algo._main, algo._stop, algo._colors)
    
    def drawSleep(self):
        sleep(self._velocity[0])
        self._main.event_generate("<<draw>>")
    
    def reset_colors(self):
        n = len(self._array)
        for i in range(n):
            self._colors[i] = self._fc
        self.drawSleep()

    @abc.abstractclassmethod
    def run(self):
        pass
    
    @abc.abstractclassmethod
    def info(self):
        pass