import tkinter as tk

import core
from view import View


class Stage(View):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Stage.__instance == None:
            Stage()
        return Stage.__instance

    def __init__(self):
        if Stage.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Stage.__instance = self

    def show(self):
        self.window.grid(row=0, column=0, pady=0, padx=0)
        self.image = tk.PhotoImage(file="inc/assets/logo.png")
        self.window.create_image(275, 50, image=self.image)

        gap = 50
        offset = 100

        for line_pair in zip(core.vertical_lines, core.horizontal_lines):
            for line in line_pair:
                self.drawLine(line, self.window, offset, gap)

    def drawLine(self, line, canvas, offset, gap):
        (x, y, a, b) = [point*gap+offset for point in [
            line.x1, line.y1, line.x2, line.y2]]
        newline = self.window.create_line(x, y, a, b, fill="#dddddd", width=2)
        canvas.tag_bind(newline, "<Button-1>", lambda event,
                        newline=newline, canvas=self.window: line.selectLine(newline, canvas))
