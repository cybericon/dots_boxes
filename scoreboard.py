import tkinter as tk
from tkinter.font import Font

import core
from view import View


class ScoreBoard(View):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ScoreBoard.__instance == None:
            ScoreBoard()
        return ScoreBoard.__instance

    def __init__(self):
        if ScoreBoard.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ScoreBoard.__instance = self

    def show(self):
        self.window.grid(row=0, column=1, pady=0, padx=0)
        self.window.create_rectangle(
            0, 0, 230, 600, fill=self.frame._dark_bg
        )
        self._heading_font = Font(family='Segoe UI', size=20)
        self._regular_font = Font(family='Segoe UI Light', size=12)
        self._primary_color = "#bdccd4"  # silver white
        self._secondary_color = "#ff931e"  # dull orange
        self.createHeading(10, text="Boxes")
        self.createBoxInfo(50,
                           text="Available Boxes \t ",
                           attach_variable=core.available_boxes())
        self.createBoxInfo(70,
                           text="Owned Boxes \t ",
                           attach_variable=core.boxes_owned())
        # Second Block
        self.createHeading(140, text="Boxes Owned")
        self.createBoxInfo(180,
                           text=f"{core.playerOne.name.upper()} \t \t ",
                           attach_variable=core.playerOne.owned)
        self.createBoxInfo(200,
                           text=f"{core.playerTwo.name.upper()} \t \t ",
                           attach_variable=core.playerTwo.owned)
        # Third Block
        self.createHeading(270, text="Current Move", color="#bdccd4")
        self.createBoxInfo(310,
                           text=f"{core.players[0].name.upper()} \t ",
                           color="#ff931e", attach_variable='')

        if core.boxes_owned() == core.total_boxes:
            if core.playerOne.owned > core.playerTwo.owned:
                text = f"{core.playerOne.name} Wins"
            elif core.playerOne.owned < core.playerTwo.owned:
                text = f"{core.playerTwo.name} Wins"
            else:
                text = "Game Drawn"
            self.createHeading(
                400, text=text)

    def createHeading(self, top_distance, text, color="#ff931e"):
        self.window.create_text(
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
        self.window.create_text(
            30,
            top_distance,
            fill=color,
            font=self._regular_font,
            text=text + f'{attach_variable}',
            anchor="nw")
