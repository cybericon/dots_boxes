import tkinter as tk


class View:

    def __init__(self):
        pass

    def config(self, frame, width, height, background):
        self.frame = frame
        self.width = width
        self.height = height
        self.bg = background
        self.window = tk.Canvas(self.frame, width=self.width,
                                height=self.height, background=self.bg)
