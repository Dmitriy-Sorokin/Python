from tkinter import *

root = Tk()

root.title('Цвета радуги')
root.iconbitmap('python.ico')
root.geometry('400x200+900+300')
l = Label(root, text='Click button')
l.pack()
e = Entry(root, justify=CENTER)
e.pack()

colors = {
    '#ff0000': 'Red',
    '#ff7d00': 'Orange',
    '#ffff00': 'Yellow',
    '#00ff00': 'Green',
    '#007dff': 'Light blue',
    '#0000ff': 'Blue',
    '#7d00ff': 'Purple',
}


class MyButtons:

    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(root, bg=hex_color, command=self.get_color)
        self.b.pack(fill=X)

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)


for k, v in colors.items():
    MyButtons(root, v, k)

root.mainloop()
