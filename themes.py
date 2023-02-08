import tkinter as tk
from tkinter import ttk

theme_window = None

def show_themes(root, set_colors_f):
    global theme_window

    if theme_window is not None and theme_window.winfo_exists():
        return

    theme_window = tk.Toplevel(root)
    theme_window.title("Seleziona tema")
    theme_window.geometry("240x70")
    theme_window.resizable(False, False)
    theme_window.grid_propagate(False)
    themes = [("Tema 1", "#533747, #5F506B, #6A6B83, #76949F, #91C1C3, #FF5733"), 
              ("Tema 2", "#aaaaaa, #bbbbbb, #cccccc, #dddddd, #eeeeee, #ffffff"), 
              ("Tema 3", "#112233, #445566, #778899, #aabbcc, #ddeeff, #001122")]
    theme_combo = ttk.Combobox(theme_window, values=[theme[0] for theme in themes], state='readonly')
    theme_combo.place(x=0, y=0, width=240, height=30) 
    theme_combo.current(0)

    squares = []
    for i in range(6):
        square = tk.Canvas(theme_window, width=20, height=20, highlightbackground='#000000')
        square.place(x=i*40, y=30, width=40, height=40)
        squares.append(square)

    def set_default_colors():
        selected_theme = theme_combo.get()
        for theme in themes:
            if theme[0] == selected_theme:
                set_colors(theme[1].split(", "))

    def set_colors(hex_values):
        selected_theme = theme_combo.get()
        for theme in themes:
            if theme[0] == selected_theme:
                colors = theme[1].split(", ")
                for i, color in enumerate(colors):
                    squares[i].configure(bg=color)
                theme_window.config(bg=colors[0])
                set_colors_f(colors)
    
    theme_combo.bind("<<ComboboxSelected>>", lambda event: set_colors(themes[theme_combo.current()][1].split(", ")))

    def on_closing():
        global theme_window
        theme_window.destroy()
        theme_window = None
        
    theme_window.after(100, set_default_colors)
    theme_window.protocol("WM_DELETE_WINDOW", on_closing)