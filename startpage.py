import tkinter as tk
from tkinter.font import Font

from core import scoreboard, stage, copyrights


class StartPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self._light_bg = "#ecf0f1"
        self._dark_bg = "#2c3e50"

        stage.config(self, width=550, height=500,
                     background=self._light_bg)

        scoreboard.config(self, width=230, height=500,
                          background=self._dark_bg)

        copyrights.config(self, width=780, height=120,
                          background=self._light_bg)

        stage.show()
        scoreboard.show()
        copyrights.show()
