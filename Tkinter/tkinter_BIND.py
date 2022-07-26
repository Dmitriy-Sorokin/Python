from tkinter import *

<<<<<<< HEAD

root =Tk()
root.geometry('400x300+1000+300')

def f_event(event, key):
    print(event)
    print('Leftclick')

e = Entry(root, justify=CENTER, font=10)
e.pack(fill=X, expand=1, ipady=10)
e.bind('<Button-1>', lambda event, key='Left click': f_event(event, key))
e.bind('<Button-2>', lambda event, key='Middle click': f_event(event, key))
e.bind('<Button-3>', lambda event, key='Left click': f_event(event, key))

root.mainloop()
=======
root = Tk()

root.geometry('800x600+900+300')

def f_event(event, key):
    print(event, key)

e = Entry(root, justify=CENTER, font=15)
e.pack(fill=X, expand=1, padx=10, pady=10)


e.bind("<Button-1>", lambda event, key='Left click': f_event(event, key))
e.bind("<Button-2>", lambda event, key='Middle click': f_event(event, key))
e.bind("<Button-3>", lambda event, key='Right click': f_event(event, key))




root.mainloop()
>>>>>>> origin/main
