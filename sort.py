import time
import random
import threading
import math

global velocity
velocity = [0.0]

global fc
global sc
global tc
fc = '#cc241d'
sc = '#ebdbb2'
tc = '#b8bb26'
othercolors = ["#928374", "#fabd2f", "#83a598", "#d3869b", "#fe8019", '#8ec07c', '#f92672', '#7fffd4', '#e1c699', '#c8a2c8']

def set_unit_colors(unitcolors):
    global fc
    global sc
    global tc
    fc = unitcolors[0]
    sc = unitcolors[1]
    tc = unitcolors[2]
