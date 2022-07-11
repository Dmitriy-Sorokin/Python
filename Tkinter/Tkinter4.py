from tkinter import *

root = Tk()

root.title('Моё не первое GUI приложение')
root.iconbitmap('python.ico')
root.geometry('800x600+900+300')
root.resizable(True, True)
root.config(bg='black')

# l = Label(root, text='Текст в строке 1\nСтрока 2\nСтрока 3\nСтрока 4\nСтрока 5\nСтрока', bg='red', fg='blue',
#           justify=LEFT, width=60, height=10, anchor=NE)
# l.pack()

# img = PhotoImage(file='1.png')
# l_logo = Label(root, image=img)
# l_logo.pack()

root.mainloop()
