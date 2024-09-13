import tkinter
from tkinter import font
"""
https://metanit.com/python/tkinter/1.1.php
"""
root = tkinter.Tk()


def show_font_families():
    for par in font.families():
        print(par)


def show_font_names():
    for par in font.names():
        print(par)


# show_font_families()
show_font_names()