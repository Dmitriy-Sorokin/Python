from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk


root = ThemedTk(theme='radiance')
root.geometry('400x300+1000+300')


ttk.Button(root, text='Button').pack(pady=10)
Entry(root).pack()


root.mainloop()