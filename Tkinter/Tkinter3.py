from tkinter import *
import time

root = Tk()

root.title('Counter')
root.iconbitmap('python.ico')
root.geometry('800x600+900+300')
root.resizable(True, True)
root.config(bg='black')


def check_time():
    btn_time['text'] = time.strftime(('%H:%M:%S'))
    # print(time.strftime('%H:$M:%s'))

clicks = 0

def counter():
    global clicks
    clicks += 1
    root.title(f'counter: {clicks}')

def plus():
    a = 10
    b = 5
    btn_plus['text'] = a + b

btn_time = Button(root, text='check time', command=check_time)
btn_time.pack()

btn_count = Button(root, text='counter', command=counter)
btn_count.pack()

btn_plus = Button(root, text='plus', command=plus)
btn_plus.pack()

root.mainloop()
