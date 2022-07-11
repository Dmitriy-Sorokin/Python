from tkinter import *

root = Tk()

def add_str():
    e.insert(END, 'Hello!')

def del_str():
    e.delete(0, END)

def get_str():
    l_text['text'] = e.get()

root.title('Моё не первое GUI приложение')
root.iconbitmap('python.ico')
root.geometry('800x600+900+300')
root.resizable(True, True)
root.config(bg='black')

l = Label(root, text='write')
l.pack()

e = Entry(root)
# e.insert(0, 'Hello')
# e.insert(END, ' World')
e.pack()

btn_add = Button(root, text='ADD', command=add_str)
btn_add.pack()

btn_del = Button(root, text='DELETE', command=del_str)
btn_del.pack()

btn_get = Button(root, text='GET', command=get_str)
btn_get.pack()


l_text = Label(root)
l_text.pack(fill=X)

root.mainloop()