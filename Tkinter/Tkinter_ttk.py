from tkinter import *
from tkinter import ttk

root = Tk()

root.title('Моё не первое GUI приложение')
root.geometry('800x600+900+300')
root.resizable(True, True)
root.config(bg='black')

s = ttk.Style()
# s.theme_use('clam')
# s.configure('.', foreground='red')
s.configure('red.TButton', foreground='red')


# btn = ttk.Button(root, text='Button 1', style='red.TButton')
# btn.pack(pady=10)
#
# btn1 = ttk.Button(root, text='Button 2', width=21)
# btn1.pack()
#
# e = ttk.Entry(root)
# e.pack()
#
# e1 = ttk.Entry(root)
# e1.pack()

def choose(event):
    select.current(0)

select = ttk.Combobox(root, values=['january', 'February', 'March', 'April', 'May'])
select.place(relx=0.5, rely=0.5, anchor=CENTER)
select.current(0)

select.bind('<<ComboboxSelected>>', choose)

root.mainloop()
