import tkinter as tk
from tkinter import ttk

theme_window = None

global themes
themes = [("Theme 1", "#282828, #282828, #ebdbb2, #cc241d"),
          ("Theme 2", "#533747, #6A6B83, #91C1C3, #FF5733"), 
          ("Theme 3", "#003C82, #12A0D7, #FFFFFF, #ffffff"), 
          ("Theme 4", "#112233, #778899, #ddeeff, #001122")]

global last
last = 0

def create_combobox_styles(combostyle):
    global themes
    for i in range(len(themes)):
        colors = themes[i][1].split(", ")
        combostyle.theme_create('Theme ' + str(i + 1), parent='clam', settings = {'TCombobox': {'configure': {
                                                                                            'selectbackground': colors[1],
                                                                                            'fieldbackground': colors[1],
                                                                                            'foreground': colors[2]
                                                                                            }}})


def show_themes(root, set_colors_f, combostyle):
    global theme_window
    global themes
    global last

    if theme_window is not None and theme_window.winfo_exists():
        return

    theme_window = tk.Toplevel(root)
    theme_window.title("Select a theme")
    theme_window.geometry("240x70")
    theme_window.resizable(False, False)
    theme_window.grid_propagate(False)
    
    theme_combo = ttk.Combobox(theme_window, values=[theme[0] for theme in themes], state='readonly')
    theme_combo.place(x=0, y=0, width=240, height=30) 
    theme_combo.current(last)

    squares = []
    for i in range(4):
        square = tk.Canvas(theme_window, width=20, height=20, highlightbackground='#000000')
        square.place(x=i*60, y=30, width=60, height=40)
        squares.append(square)

    def set_default_colors():
        selected_theme = theme_combo.get()
        for theme in themes:
            if theme[0] == selected_theme:
                set_colors(theme[1].split(", "))

    def set_colors(hex_values):
        selected_theme = theme_combo.get()
        
        for i, theme in enumerate(themes):
            if theme[0] == selected_theme:
                colors = theme[1].split(", ")
                
                for j, color in enumerate(colors):
                    squares[j].configure(bg=color)
                
                theme_window.config(bg=colors[0])
                set_colors_f(colors)
                combostyle.theme_use(str(theme[0]))

                global last
                last = i

    theme_combo.bind("<<ComboboxSelected>>", lambda event: set_colors(themes[theme_combo.current()][1].split(", ")))

    def on_closing():
        global theme_window
        theme_window.destroy()
        theme_window = None
        
    theme_window.after(100, set_default_colors)
    theme_window.protocol("WM_DELETE_WINDOW", on_closing)