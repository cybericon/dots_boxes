import tkinter as tk
from tkinter.font import Font

from line import VerticalLine, HorizontalLine
from box import Box
from config import BOXES, available_boxes, boxes_owned, SIZE, players, playerOne, playerTwo


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self._heading_font = Font(family='Segoe UI', size=20)
        self._regular_font = Font(family='Segoe UI Light', size=12)
        self._primary_color = "#bdccd4"  # silver white
        self._secondary_color = "#ff931e"  # dull orange
        self._light_bg = "#ecf0f1"
        self._dark_bg = "#2c3e50"

        self.canvas = tk.Canvas(
            self, width=550, height=600, background=self._light_bg)
        self.canvas.grid(row=0, column=0, pady=0, padx=0)
        self.__getCanvasContents()

        """ Scoreboard related layout to be cleaned up """
        self.scoreboard = tk.Canvas(self, width=230, height=600,
                                    background=self._dark_bg)
        self.scoreboard.grid(row=0, column=1, pady=0, padx=0)
        self.__getScoreBoardContents()

    def __getScoreBoardContents(self):
        # First Block
        self.createHeading(10, text="Boxes")
        self.createBoxInfo(50,
                           text="Available Boxes \t ", attach_variable=available_boxes)
        self.createBoxInfo(70,
                           text="Owned Boxes \t ", attach_variable=boxes_owned)
        # Second Block
        self.createHeading(140, text="Boxes Owned")
        self.createBoxInfo(180,
                           text=f"{playerOne.name} \t \t ")
        self.createBoxInfo(200,
                           text=f"{playerTwo.name} \t \t ")
        # Third Block
        self.createHeading(270, text="Current Move", color="#bdccd4")
        self.createBoxInfo(310,
                           text="Player One / Two \t ", color="#ff931e")

    def __getCanvasContents(self):
        self.image = tk.PhotoImage(file="inc/assets/logo.png")
        self.canvas.create_image(275, 50, image=self.image)

        size = SIZE
        gap = 50
        offset = 100

        vertical_lines = [VerticalLine([x, y, x, y + 1], self.canvas)
                          for x in range(size + 1)for y in range(size)]

        horizontal_lines = [HorizontalLine([x, y, x + 1, y], self.canvas)
                            for x in range(size) for y in range(size + 1)]

        for line_pair in zip(vertical_lines, horizontal_lines):
            for line in line_pair:
                line.drawLine(self.canvas, offset, gap)

    def createHeading(self, top_distance, text, color="#ff931e"):
        self.scoreboard.create_text(
            30,
            top_distance,
            font=self._heading_font,
            text=text,
            fill=color,
            anchor="nw")

    def createBoxInfo(self,
                      top_distance,
                      text,
                      color="#bdccd4",
                      attach_variable=0):
        self.scoreboard.create_text(
            30,
            top_distance,
            fill=color,
            font=self._regular_font,
            text=text + f'{attach_variable}',
            anchor="nw")
