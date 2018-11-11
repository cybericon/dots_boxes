""" 
Core File to setup initial state of Game and its entities
And update status of game with each move by the player
"""

from stage import Stage
from copyrights import Copyrights
from scoreboard import ScoreBoard
from player import Player
from box import Box
from line import VerticalLine, HorizontalLine



p1_name = input("Player 1 name: ")
p2_name = input("Player 2 name: ")

level = input("Please Select Level \n(Beginner : B, Intermediate : I, Expert : E) : ")
level = level.upper()[0]

while (level not in ['B', 'I', 'E']):
    print("!!! INCORRECT SELECTION !!!")
    level = input("Please Select Level \n(Beginner : B, Intermediate : I, Expert : E) : ")
    level = level.upper()[0]

if level== 'B':
    size = 4
elif level == 'I':
    size = 6
elif level == 'E':
    size = 8



""" Setting up Players """

playerOne = Player(p1_name, "#ff931e")
playerTwo = Player(p2_name,  "#2c3e50")
players = [playerOne, playerTwo]


def getPlayer():
    return players[0]


""" Setting up Boxes """

total_boxes = size * size
boxes = [[Box(x, y) for y in range(size)] for x in range(size)]


def boxes_owned():
    return len([box.owned for row in boxes for box in row if box.owned is not None])


def available_boxes():
    return total_boxes - boxes_owned()


""" Setting up Lines """

vertical_lines = [VerticalLine([x, y, x, y + 1])
                  for x in range(size + 1)for y in range(size)]

horizontal_lines = [HorizontalLine([x, y, x + 1, y])
                    for x in range(size) for y in range(size + 1)]


""" Setting up Start page contents """
stage = Stage()
scoreboard = ScoreBoard()
copyrights = Copyrights()


def updateMove(line, canvas):
    global players
    turn = 0
    for box, wall in zip(line.boxes, line.walls):
        box.walls[wall] = 1
        if box.getScore() == 4:
            box.owned = players[0].name
            players[0].owned += 1
            turn += 1
            box.displayOwner(canvas, 100, 50)
    if turn == 0:
        players[0], players[1] = players[1], players[0]
    scoreboard.show()
