from tkinter import *

root = Tk()

root.title('Tекстовый редактор')
root.iconbitmap('python.ico')
root.geometry('800x600+900+300')


main_menu = Menu(root)
root.config(menu=main_menu)

# main_menu.add_command(label='File')

def abaut_programm():
    print("REbus")

#File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='open')
file_menu.add_command(label='save')
file_menu.add_separator()
file_menu.add_command(label='exit')
main_menu.add_cascade(label='file', menu=file_menu)

# About
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label='link site')
help_menu_sub.add_command(label='link site offline')
help_menu.add_cascade(label='help', menu=help_menu_sub)
help_menu.add_command(label='programm info', command=abaut_programm)
main_menu.add_cascade(label='Synopsis', menu=help_menu)

# f_menu = Frame(root, bg='#1F252A', height=40)
f_text = Frame(root)
# f_menu.pack(fill=X)
f_text.pack(fill=BOTH, expand=1)



t = Text(f_text, bg='#343D46', fg='#C6DEC1', padx=10, pady=10, wrap=WORD, insertbackground='#EDA756',
         selectbackground='#4E5A65', spacing3=10)
t.pack(fill=BOTH, expand=1, side=LEFT)


scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()
