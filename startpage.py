import tkinter as tk
from tkinter.font import Font

from core import scoreboard, stage


class StartPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self._light_bg = "#ecf0f1"
        self._dark_bg = "#2c3e50"

        stage.config(self, width=550, height=600,
                     background=self._light_bg)

        scoreboard.config(self, width=230, height=600,
                          background=self._dark_bg)

        stage.show()
        scoreboard.show()
