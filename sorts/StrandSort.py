from sorts.Algorithm import Algorithm
import time

class StrandSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    
    def run(self, superlist = None, ric = [0]):
        if superlist == None:
            superlist = self._array
        if(self._stop[0] or len(superlist) == 0):
            return
        else:
            if(ric[0] == 0):
                superlist = self._array.copy()
                self._array.clear()
            sublist = []
            sublist.append(superlist.pop(0))
            i = 0
            idx = 0
            while i < len(superlist):
                if(self._stop[0]):
                    return
                if(superlist[i] > sublist[idx]):
                    sublist.append(superlist.pop(i))
                    i -= 1
                    idx += 1
                i += 1

            if ric[0] == 0:
                i = 0
                while i < len(sublist):
                    if(self._stop[0]):
                        return
                    self._array.append(sublist[i])
                    self.drawSleep()
                    if(self._stop[0]):
                        return
                    i += 1
            else:
                subend = len(sublist) - 1
                solstart = 0;
                while len(sublist) > 0:
                    if(self._stop[0]):
                        return
                    if sublist[subend] > self._array[solstart]:
                        solstart += 1
                    else:
                        if(self._stop[0]):
                            return
                        self._array.insert(solstart, sublist.pop(subend))
                        self.drawSleep()
                        if(self._stop[0]):
                            return
                        subend -= 1
                        solstart = 0
            
            ric[0] += 1
            time.sleep(self._velocity[0] * 2)
            self.run(superlist, ric)

        
    def info(self):
        pass