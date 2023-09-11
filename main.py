from tkinter import *
from tk_html_widgets import HTMLLabel

class Main:
    def __init__(self):
        self.items = ['body', 'html', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                 'li', 'br', 'ol', 'ul', 'img', 'em', 'a', 'b', 'p',
                 'div', 'span', 'i', 'u', 'em', 'pre', 'code', 'style', 'href', 'width', 'height', 'type'
        ]

    def show(self, master):
        master.geometry("640x480-100-100")
        master.title("Html Editor")
        
        menubar = Menu(master)
        filemenu = Menu(master, tearoff=0)
        filemenu.add_command(label="exit Alt+F4", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)

        body = Button(master, text="body")
        body.pack()        

root = Tk()
Main().show(root)
root.mainloop()