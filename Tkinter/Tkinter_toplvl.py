from tkinter import *

root = Tk()
root.geometry('400x300+1000+300')

def open_win():
    win = Toplevel()
    win.geometry('200x100+1200+450')
    # win.overrideredirect(True)
    win.grab_set()
    l = Label(win, text='Hello from toplevel', bg='#000', fg='#fff')
    l.pack(expand=1, fill=BOTH)
    win.after(3000, lambda: win.destroy())

Button(root, text='Open', command=open_win, padx=40, pady=5).place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()