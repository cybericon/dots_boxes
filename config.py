from box import Box
from player import Player


SIZE = 4

BOXES = [[Box(x, y) for x in range(SIZE)] for y in range(SIZE)]
playerOne = Player("Touseef", "#ff931e")
playerTwo = Player("Furqan",  "#2c3e50")
players = [playerOne, playerTwo]

total_boxes = SIZE * SIZE


def boxes_owned():
    global BOXES
    return len([box.owned for row in BOXES for box in row if box.owned is not None])


def available_boxes():
    global total_boxes
    return total_boxes - boxes_owned()
