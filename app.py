import tkinter as tk
from tkinter.font import Font

from startpage import StartPage


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.app_icon = tk.PhotoImage(file=r'inc/assets/app.ico')
        self.tk.call('wm', 'iconphoto', self._w, self.app_icon)
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nwes")
        container.grid_rowconfigure(2, weight=1)
        container.grid_columnconfigure(2, weight=1)

        self.frames = {}

        frame = StartPage(container)
        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = App()
app.resizable(0, 0)
app.title("Dots and Boxes")
app.mainloop()
