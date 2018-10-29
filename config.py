from box import Box
from player import Player


SIZE = int(input("Please enter grid size (min 4 max 8) : "))
p1_name = input("Player 1 name: ")
p2_name = input("Player 2 name: ")

BOXES = [[Box(x, y) for x in range(SIZE)] for y in range(SIZE)]
playerOne = Player(p1_name, "#ff931e")
playerTwo = Player(p2_name,  "#2c3e50")
players = [playerOne, playerTwo]

total_boxes = SIZE * SIZE


def boxes_owned():
    global BOXES
    return len([box.owned for row in BOXES for box in row if box.owned is not None])


def available_boxes():
    global total_boxes
    return total_boxes - boxes_owned()
