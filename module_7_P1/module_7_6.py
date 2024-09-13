import os
import tkinter as tk
from tkinter import filedialog


def file_select():
    f_name = filedialog.askopenfile(initialdir='/', title='Select file',
                                    filetypes=(('Text', 'txt'), ('all', '*')))
    text['text'] += ' ' + f_name.name.rsplit('/', 1)[1]
    os.startfile(f_name.name)


root = tk.Tk()
root.title('Проводник')
root.geometry('350x350')
root.configure(bg='Grey')
root.resizable(width=False, height=False)
text = tk.Label(root, text='Файл', width=40, height=2, background='Silver', font='Cambria 11 bold roman')
text.grid(column=0, row=1)
bt_select = tk.Button(root, width=20, height=2, text='Выбрать файл',
                      font='Arial 11 bold roman', command=file_select)
bt_select.grid(column=0, row=2)

root.mainloop()
