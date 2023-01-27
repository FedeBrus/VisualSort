from tkinter import *
from tkinter import ttk
from tkinter import font
import random as rnd
import sorts.bubble
import sorts.bogo
import sorts.counting
import sorts.gnome
import sorts.heap
import sorts.insertion
import sorts.intro
import sorts.merge
import sorts.radix
import sorts.selection
import sorts.shell
import sorts.quick
import sorts.sleep
from threading import Thread

stop = [False]


def sort_array(alg):
    global stop

    btn_sort["state"] = "disabled"
    btn_shuffle["state"] = "disabled"

    def sort():
        stop[0] = False
        match (alg):
            case 'Bubble sort':
                sorts.bubble.bubble_sort(array, main, stop)
            case 'Bogo sort':
                sorts.bogo.bogo_sort(array, main, stop)
            case 'Counting sort':
                sorts.counting.counting_sort(array, main, stop)
            case 'Gnome sort':
                sorts.gnome.gnome_sort(array, main, stop)
            case 'Heap sort':
                sorts.heap.heap_sort(array, main, stop)
            case 'Insertion sort':
                sorts.insertion.insertion_sort(array, main, stop)
            case 'Intro sort':
                sorts.intro.intro_sort(array, main, stop)
            case 'Merge sort':
                sorts.merge.merge_sort(array, main, stop, 0, len(array) - 1)
            case 'Radix sort':
                sorts.radix.radix_sort(array, main, stop)
            case 'Selection sort':
                sorts.selection.selection_sort(array, main, stop)
            case 'Shell sort':
                sorts.shell.shell_sort(array, main, stop)
            case 'Sleep sort':
                sorts.sleep.sleep_sort(array, main, stop)
            case 'Quick sort':
                sorts.quick.quick_sort(array, main, stop, 0, len(array) - 1)

        btn_sort['state'] = "normal"
        btn_shuffle['state'] = "normal"

    Thread(target=sort, daemon=True).start()


def draw_event(event):
    draw_array()

# Clears canvas and draws the new array
def draw_array():
    global array
    canvas.delete('all')
    rectX = 1200 / len(array)
    rectY = 600 / (len(array) + 1)
    rX = 0
    rY = 600
    for i in array:
        canvas.create_rectangle(
            rX, rY, rX + rectX, rY - (rectY * i), fill='red')
        rX += rectX

    main.update_idletasks()

# Fisher-Yates shuffle
def shuffle_array(array):
    for i in range(0, len(array) - 1):
        j = rnd.randint(i, len(array) - 1)
        array[j], array[i] = array[i], array[j]

# Generates an array whose elements have distinct values from 1 to size
def generate_array(size):
    global array
    array = [i for i in range(1, size + 1)]
    shuffle_array(array)
    draw_array()


def stop_thread():
    global stop
    stop[0] = True


# Main window
main = Tk()
main.title("Visual Sort")
main.geometry("1200x800")
main.resizable(False, False)
main.protocol("WM_DELETE_WINDOW", )

# Options Frame
options = Frame(main, width=1200, height=200, bg='gray')
options.grid_propagate(False)
options.pack()

# Algs ComboBox
selected_alg = StringVar()
algorithms = ttk.Combobox(options, textvariable=selected_alg)
algorithms['values'] = ('Bubble sort', 'Bogo sort', 'Counting sort', 'Gnome sort',
                        'Heap sort', 'Insertion sort', 'Intro sort', 'Merge sort', 
                        'Radix sort', 'Selection sort', 'Shell sort', 'Sleep sort',
                        'Quick sort')
algorithms.current(0)
algorithms.grid(row=0, column=0)

# Size ComboBox
selected_size = StringVar()
sizes = ttk.Combobox(options, textvariable=selected_size)
sizes['values'] = ('10', '50', '100', '200', '400', '600')
sizes.current(0)
sizes.grid(row=0, column=1)

# Generate Button
btn_shuffle = Button(options, command=lambda: generate_array(
    int(selected_size.get())), text='Shuffle')
btn_shuffle.grid(row=0, column=2)

# Generate Button
btn_sort = Button(options, command=lambda: sort_array(
    selected_alg.get()), text='Sort')
btn_sort.grid(row=0, column=3)

# Slider for sorting speed
def getSpeed(val):
    speed = val
    return None
    
minSpeed = 0.5
maxSpeed = 2

slider = Scale(options, from_=minSpeed, to=maxSpeed, orient=HORIZONTAL, length=200, command=getSpeed, resolution = 0.5, foreground='#a32929', bg = '#1c1c1c', activebackground = '#801410')
slider.set(1)
slider.config(label='Velocità di ordinamento')
font_style = font.Font(family='Consolas', size=11)
slider.config(font=font_style)
slider.grid(row = 0, column = 5)

btn_stop = Button(options, command=stop_thread, text="Stop")
btn_stop.grid(row=0, column=4)

# Sort Canvas
canvas = Canvas(main, width=1200, height=600, bg='black')
canvas.pack()

generate_array(10)
main.bind("<<draw>>", draw_event)
main.mainloop()
