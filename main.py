from tkinter import *
from tkinter import ttk
from tkinter import font
import random as rnd
from sort import *
from themes import *
from threading import Thread
from pygame import mixer
from pysound import oscillators
from pysound import soundfile
from pysound import buffer
from os import remove
from themes import *

stop = [False]
sound = False
global unitcolor 
unitcolor = '#FF5733'

def sort_array(alg):
    global stop
    global colors
    
    sizes["state"] = "disabled"
    algorithms["state"] = "disabled"
    btn_stop["state"] = "normal"
    btn_sort["state"] = "disabled"
    btn_shuffle["state"] = "disabled"

    if(alg == 'Sleep sort'):
        btn_stop["state"] = "disabled"
        slider.set(0)
        slider["state"] = "disabled"
    
    def sort():
        stop[0] = False
        match (alg):
            case 'Bubble sort':
                bubble_sort(array, main, stop, colors)
            case 'Bogo sort':
                bogo_sort(array, main, stop, colors)
            case 'Bucket sort':
                bucket_sort(array, main, stop, colors)
            case 'Cocktail Shaker sort':
                cocktailshaker_sort(array, main, stop, colors)
            case 'Comb sort':
                comb_sort(array, main, stop, colors)
            case 'Counting sort':
                counting_sort(array, main, stop, colors)
            case 'Cycle sort':
                cycle_sort(array, main, stop, colors)
            case 'Gnome sort':
                gnome_sort(array, main, stop, colors)
            case 'Heap sort':
                heap_sort(array, main, stop, colors)
            case 'Insertion sort':
                insertion_sort(array, main, stop, colors)
            case 'Intro sort':
                intro_sort(array, main, stop, colors)
            case 'Merge sort':
                merge_sort(array, main, stop, 0, len(array) - 1, colors)
            case 'Odd-Even sort':
                oddeven_sort(array, main, stop, colors)
            case 'Pancake sort':
                pancake_sort(array, main, stop, colors)
            case 'Radix 10 LSD sort':
                radix10LSD_sort(array, main, stop, colors)
            case 'Radix 2 LSD sort':
                radix2LSD_sort(array, main, stop, colors)
            case 'Selection sort':
                selection_sort(array, main, stop, colors)
            case 'Shell sort':
                shell_sort(array, main, stop, colors)
            case 'Sleep sort':
                sleep_sort(array, main, stop)
            case 'Slow sort':
                slow_sort(array, main, stop, colors, 0, len(array) - 1)
            case 'Stooge sort':
                stooge_sort(array, main, stop, 0, len(array) - 1, colors)
            case 'Strand sort':
                strand_sort(array, array, [0], main, stop, colors)
            case 'Tree sort':
                tree_sort(array, main, stop)
            case 'Quick sort':
                quick_sort(array, main, stop, 0, len(array) - 1, colors)

        draw_final()
        btn_sort["state"] = "normal"
        btn_shuffle["state"] = "normal"
        btn_stop["state"] = "disabled"
        sizes["state"] = "readonly"
        algorithms["state"] = "readonly"
        slider["state"] = "normal"
        reset_colors(array, colors, main)
        
        try:
            remove("sound.wav")
        except IOError:
            pass
        
    Thread(target=sort, daemon=True).start()

def draw_event(event):
    draw_array()

# Clears canvas and draws the new array
def draw_array():
    global array
    global colors
    global sound
    canvas.delete('all')
    rectX = 1600 / len(array) if len(array) else 1
    rectY = 600 / (max(max(array) if len(array) > 0 else 1, len(array)) + 1)
    rX = 0
    rY = 600
    
    if(len(array) > len(colors)):
        array = array[0:-1:].copy()

    for i in range(len(array)):
        color = colors[i]
        canvas.create_rectangle(
            rX, rY, rX + rectX, rY - (rectY * array[i]), fill=color)
        rX += rectX

    if sound:
        mixer.music.unload()
        params = buffer.BufferParams(400)
        pitch = 1
        pitch += sum([array[i] for i, x in enumerate(colors) if colors[i] == sc])
        data = oscillators.sine_wave(params, int(pitch / max(array) * 100) * 10, 0.7)
        soundfile.save(params, "sound.wav", data)
        mixer.music.load("sound.wav")
        mixer.music.play()
        
    main.update_idletasks()

# Draw the array when the sort has finished
def draw_final():
    global colors, array
    if stop[0]:
        return
    colors = [tc for x in array]
    for i, x in enumerate(array):
        colors[i] = sc
        main.event_generate("<<draw>>")
        colors[i] = tc
        time.sleep(0.01)
        if stop[0]:
            return

# Fisher-Yates shuffle
def shuffle_array(array):
    global colors
    colors = ['#cc241d' for i in range(len(array))]
    for i in range(0, len(array) - 1):
        j = rnd.randint(i, len(array) - 1)
        array[j], array[i] = array[i], array[j]

# Generates an array of distinct values from 1 to size
def generate_array(size):
    global array
    global colors
    colors = ['#cc241d' for i in range(size)]
    array = [i for i in range(1, size + 1)]
    shuffle_array(array)
    draw_array()
    
def stop_thread():
    global stop
    global array
    global colors

    n = int(selected_size.get()) 
    if(len(array) != n):
        for i in range(n):
            if i + 1 not in array:
                array.append(i + 1)

    for i in range(n):
        colors[i] = '#cc241d'

    draw_array()
    stop[0] = True


def toggle_sound():
    global sound
    sound = not sound
    btn_sound["text"] = "Toggle sound off" if sound else "Toggle sound on"

# Main window
main = Tk()
main.title("Visual Sort")
main.geometry("1600x800")
main.resizable(False, False)
main.protocol("WM_DELETE_WINDOW", )

mixer.init()

# Colors
dark = '#282828'
medium = '#ebdbb2'
light = '#ebdbb2'

# Font
font_style = font.Font(family='Consolas', size=12)
font_icon = font.Font(family='Arial', size = 20)

# Options Frame
options = Frame(main, width=1600, height=200, bg=dark)
options.grid_propagate(False)
options.pack()

# Algs ComboBox
selected_alg = StringVar()
algorithms = ttk.Combobox(options, textvariable=selected_alg, font=font_style, state='readonly')
algorithms['values'] = ('Bubble sort', 'Bogo sort', 'Bucket sort', 'Cocktail Shaker sort',
                        'Comb sort', 'Counting sort', 'Cycle sort', 'Gnome sort', 'Heap sort', 'Insertion sort',
                        'Intro sort', 'Merge sort', 'Odd-Even sort', 'Pancake sort', 'Radix 10 LSD sort',
                        'Radix 2 LSD sort', 'Selection sort', 'Shell sort', 'Sleep sort', 'Slow sort',
                        'Strand sort', 'Stooge sort', 'Tree sort', 'Quick sort')
algorithms.current(0)
algorithms.place(x=100, y=50, width=240, height=50)

# Size ComboBox
selected_size = StringVar()
sizes = ttk.Combobox(options, textvariable=selected_size, font=font_style, state='readonly')
sizes['values'] = ('10', '40', '80', '100', '200', '400', '800')
sizes.current(3)
sizes.place(x=100, y=100, width=240, height=50)
selected_size.trace("w", lambda x, y, z: generate_array(int(selected_size.get())))

# Info Button
btn_info = Button(options, text="ⓘ", bg=dark, fg=light, font=font_icon)
btn_info.place(x=30, y=50, width=50, height=50)

# Combobox Styles
combostyle = ttk.Style()
create_combobox_styles(combostyle)
combostyle.theme_use('Theme 1')

# Themes Button
def set_colors(colors):
    dark, medium, light, unitcolor = colors

    options.config(bg=dark)
    btn_info.config(bg=dark, fg=light)
    btn_themes.config(bg=dark, fg=light)
    btn_sound.config(bg=dark, fg=light)
    btn_shuffle.config(bg=dark, fg=light)
    btn_sort.config(bg=dark, fg=light)
    btn_stop.config(bg=dark, fg=light)
    slider.config(bg=dark, fg=light, activebackground=medium, highlightbackground=medium)
    canvas.config(bg=dark, highlightbackground=medium)

btn_themes = Button(options, command=lambda: show_themes(main, set_colors, combostyle), text="★", bg=dark, fg=light, font=font_icon)
btn_themes.place(x=30, y=100, width=50, height=50)

# Generate Button
btn_shuffle = Button(options, command=lambda: generate_array(
    int(selected_size.get())), text='Shuffle', bg=dark, fg=light, font=font_style)
btn_shuffle.place(x=440, y=50, width=240, height=100)

# Sort Button
btn_sort = Button(options, command=lambda: sort_array(
    selected_alg.get()), text='Sort', bg=dark, fg=light, font=font_style)
btn_sort.place(x=680, y=50, width=240, height=100)

# Sound button
btn_sound = Button(options, command=toggle_sound, text='Toggle sound on', bg=dark, fg=light, font=font_style)
btn_sound.place(x=680, y=10, width=240, height=40)

# Stop Button
btn_stop = Button(options, command=stop_thread, text="Stop", bg=dark, fg=light, font=font_style)
btn_stop.place(x=920, y=50, width=240, height=100)
btn_stop['state'] = "disabled"

# Slider for sorting speed
def getSpeed(val):
    from sort import velocity
    velocity[0] = float(2**int(val) / 1000)

minDelay = 0
maxDelay = 10

slider = Scale(options, from_=minDelay, to=maxDelay, orient=HORIZONTAL, length=200, command=getSpeed,
                resolution=1, foreground=light, bg=dark, activebackground=medium, highlightbackground=medium)
slider.set(0)
slider.config(label='Delay', font=font_style)
slider.place(x=1260, y=50, width=240, height=100)

# Sort Canvas
canvas = Canvas(main, width=1600, height=600, bg=dark, highlightthickness=3, highlightbackground=medium)
canvas.pack()

generate_array(100)
main.bind("<<draw>>", draw_event)
main.mainloop()
