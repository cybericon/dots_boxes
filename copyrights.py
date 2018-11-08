import tkinter as tk
from tkinter.font import Font

import core
from view import View


class Copyrights(View):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Copyrights.__instance == None:
            Copyrights()
        return Copyrights.__instance

    def __init__(self):
        if Copyrights.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Copyrights.__instance = self

    def show(self):
        self._font = Font(family='Segoe UI Light', size=14)
        self.window.grid(row=1, column=0, columnspan=2, pady=0, padx=0)
        self.image = tk.PhotoImage(file="inc/assets/group_logo.png")
        self.window.create_image(780/2, 50, image=self.image)
        self.window.create_text(
            780/2, 110, text="Zahra, Mishkat, Taha, Sarmad, Wajihullah", font=self._font, fill="#2c3e50")
