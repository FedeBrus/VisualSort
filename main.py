from tkinter import *
from tkinter import ttk
from tkinter import font
import random as rnd
from sort import *
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
                bubble_sort(array, main, stop)
            case 'Bogo sort':
                bogo_sort(array, main, stop)
            case 'Bucket sort':
                bucket_sort(array, main, stop)
            case 'Cocktail Shaker sort':
                cocktailshaker_sort(array, main, stop)
            case 'Comb sort':
                comb_sort(array, main, stop)
            case 'Counting sort':
                counting_sort(array, main, stop)
            case 'Gnome sort':
                gnome_sort(array, main, stop)
            case 'Heap sort':
                heap_sort(array, main, stop)
            case 'Insertion sort':
                insertion_sort(array, main, stop)
            case 'Intro sort':
                intro_sort(array, main, stop)
            case 'Merge sort':
                merge_sort(array, main, stop, 0, len(array) - 1)
            case 'Odd-Even sort':
                oddeven_sort(array, main, stop)
            case 'Radix 10 LSD sort':
                radix10LSD_sort(array, main, stop)
            case 'Radix 2 LSD sort':
                radix2LSD_sort(array, main, stop)
            case 'Selection sort':
                selection_sort(array, main, stop)
            case 'Shell sort':
                shell_sort(array, main, stop)
            case 'Sleep sort':
                sleep_sort(array, main, stop)
            case 'Tree sort':
                tree_sort(array, main, stop)
            case 'Quick sort':
                quick_sort(array, main, stop, 0, len(array) - 1)

        btn_sort['state'] = "normal"
        btn_shuffle['state'] = "normal"

    Thread(target=sort, daemon=True).start()


def draw_event(event):
    draw_array()

# Clears canvas and draws the new array
def draw_array():
    global array
    canvas.delete('all')
    rectX = 1600 / len(array)
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
main.geometry("1600x800")
main.resizable(False, False)
main.protocol("WM_DELETE_WINDOW", )

# Colors
blk = '#1c1c1c'
rd = '#a32929'

# Font
font_style = font.Font(family='Consolas', size=12)

# Options Frame
options = Frame(main, width=1600, height=200, bg=blk)
options.grid_propagate(False)
options.pack()

# Combobox style
combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='clam', settings = {'TCombobox': {'configure': {
                                                                                            'selectbackground': blk,
                                                                                            'fieldbackground': blk,
                                                                                            'foreground': 'white'
                                                                                            }}})
combostyle.theme_use('combostyle')

# Algs ComboBox
selected_alg = StringVar()
algorithms = ttk.Combobox(options, textvariable=selected_alg, font=font_style, state='readonly')
algorithms['values'] = ('Bubble sort', 'Bogo sort', 'Bucket sort', 'Cocktail Shaker sort',
                        'Comb sort', 'Counting sort', 'Gnome sort', 'Heap sort', 'Insertion sort',
                        'Intro sort', 'Merge sort', 'Odd-Even sort', 'Radix 10 LSD sort',
                        'Radix 2 LSD sort',
                        'Selection sort', 'Shell sort', 'Sleep sort', 'Tree sort', 'Quick sort')
algorithms.current(0)
algorithms.place(x=100, y=50, width=240, height=50)

# Size ComboBox
selected_size = StringVar()
sizes = ttk.Combobox(options, textvariable=selected_size, font=font_style, state='readonly')
sizes['values'] = ('10', '40', '80', '100', '200', '400', '800')
sizes.current(3)
sizes.place(x=100, y=100, width=240, height=50)

# Generate Button
btn_shuffle = Button(options, command=lambda: generate_array(
    int(selected_size.get())), text='Shuffle', bg=blk, fg='white', font=font_style)
btn_shuffle.place(x=440, y=50, width=240, height=100)

# Generate Button
btn_sort = Button(options, command=lambda: sort_array(
    selected_alg.get()), text='Sort', bg=blk, fg='white', font=font_style)
btn_sort.place(x=680, y=50, width=240, height=100)

# Stop Button
btn_stop = Button(options, command=stop_thread, text="Stop", bg=blk, fg='white', font=font_style)
btn_stop.place(x=920, y=50, width=240, height=100)

# Slider for sorting speed
def getSpeed(val):
    from sort import velocity
    velocity[0] = float(val)
    
minSpeed = 0.001
maxSpeed = 1

slider = Scale(options, from_=minSpeed, to=maxSpeed, orient=HORIZONTAL, length=200, command=getSpeed,
                 resolution=0.001, foreground='white', bg=blk, activebackground='#801410')
slider.set(0.001)
slider.config(label='Velocità', font=font_style)
slider.place(x=1260, y=50, width=240, height=100)

# Sort Canvas
canvas = Canvas(main, width=1600, height=600, bg=blk)
canvas.pack()

generate_array(100)
main.bind("<<draw>>", draw_event)
main.mainloop()
