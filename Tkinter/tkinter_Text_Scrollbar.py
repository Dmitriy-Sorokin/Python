from tkinter import *

root = Tk()

root.title('Tекстовый редактор')
root.iconbitmap('python.ico')
root.geometry('800x600+900+300')

f_menu = Frame(root, bg='#1F252A', height=40)
f_text = Frame(root)
f_menu.pack(fill=X)
f_text.pack(fill=BOTH, expand=1)

l_menu = Label(f_menu, text='Menu', bg='#2B3239', fg='#C6DEC1', font='Arial 10')
l_menu.place(x=10, y=10)

t = Text(f_text, bg='#343D46', fg='#C6DEC1', padx=10, pady=10, wrap=WORD, insertbackground='#EDA756',
         selectbackground='#4E5A65', spacing3=10)
t.pack(fill=BOTH, expand=1, side=LEFT)


scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()
