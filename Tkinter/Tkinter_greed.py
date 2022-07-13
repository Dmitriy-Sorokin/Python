from tkinter import *

root = Tk()

root.title('Моё не первое GUI приложение')
root.iconbitmap('python.ico')
# root.geometry('800x600+900+300')

# f = Frame(root)
# f.pack()
#
# btn_list = [
#     '7', '8', '9',
#     '4', '5', '6',
#     '1', '2', '3',
#     '0'
# ]
#
# row = 0
# column = 0
#
#
# for i in btn_list:
#     if i == "0":
#         Button(f, text=i, padx=50, pady=30).grid(row=row, columnspan=3)
#     else:
#         Button(f, text=i, padx=50, pady=30).grid(row=row, column=column)
#     column += 1
#     if column == 3:
#         column = 0
#         row += 1

# btn7 = Button(f, text='7', padx=50, pady=30)
# btn7.grid(row=0, column=0)
# btn8 = Button(f, text='8', padx=50, pady=30)
# btn8.grid(row=0, column=1)
# btn9 = Button(f, text='9', padx=50, pady=30)
# btn9.grid(row=0, column=2)
# btn4 = Button(f, text='4', padx=50, pady=30)
# btn4.grid(row=1, column=0)
# btn5 = Button(f, text='5', padx=50, pady=30)
# btn5.grid(row=1, column=1)
# btn6 = Button(f, text='6', padx=50, pady=30)
# btn6.grid(row=1, column=2)
# btn1 = Button(f, text='1', padx=50, pady=30)
# btn1.grid(row=2, column=0)
# btn2 = Button(f, text='2', padx=50, pady=30)
# btn2.grid(row=2, column=1)
# btn3 = Button(f, text='3', padx=50, pady=30)
# btn3.grid(row=2, column=2)
# btn0 = Button(f, text='0', padx=50, pady=30)
# btn0.grid(row=3, column=1)


l_user = Label(root, text='Login:').grid(row=0, column=0, pady=10, padx=10, sticky=E)
e_user = Entry(root).grid(row=0, column=1, columnspan=2, sticky=W+E)

l_pass = Label(root, text='Password:').grid(row=1, column=0, pady=10, padx=10, sticky=E)
e_pass = Entry(root, show='*').grid(row=1, column=1, columnspan=2, sticky=W+E)

btn_login = Button(root, text='Вход', padx=20).grid(row=2, column=0, pady=10, padx=10)
btn_reg = Button(root, text='Регистрация', padx=5).grid(row=2, column=1)
btn_forgot = Button(root, text='Восстоновление пароля', padx=5).grid(row=2, column=2, padx=10)


root.mainloop()
