from sorts.Algorithm import Algorithm
import time

class BST:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def insert(self, val):
        if self.value == None:
            self.value = val
        else:
            if val < self.value:
                if self.left == None:
                    self.left = BST()
                self.left.insert(val)
            else:
                if self.right == None:
                    self.right = BST()
                self.right.insert(val)

    def ascending(self, array, main, stop, velocity):
        if(stop[0]):
            return
        if self.value != None:
            if self.left == None:
                self.left = BST()
            self.left.ascending(array, main, stop, velocity)
            
            if(stop[0]):
                return
            array.append(self.value)
            main.event_generate("<<draw>>")
            time.sleep(velocity[0])
            if(stop[0]):
                return

            if self.right == None:
                self.right = BST()
            self.right.ascending(array, main, stop, velocity)

class TreeSort(Algorithm):
    def __init__(self, array, main, stop, colors) -> None:
        super().__init__(array, main, stop, colors)
    


    
    def run(self):
        tree = BST()
        i = 0
        n = len(self._array)
        while i < n:
            tree.insert(self._array.pop(0))
            self.drawSleep()
            if(self._stop[0]):
                return
            i += 1

        tree.ascending(self._array, self._main, self._stop, self._velocity)
    
    def info(self):
        pass