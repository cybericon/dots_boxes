from box import Box
from player import Player


SIZE = 8
BOXES = [[Box(x, y) for x in range(SIZE)] for y in range(SIZE)]
playerOne = Player("Touseef", "#ff931e")
playerTwo = Player("Furqan",  "#2c3e50")
players = [playerOne, playerTwo]

boxes_owned = len(
    [box.owned for row in BOXES for box in row if box.owned is not None])

total_boxes = SIZE * SIZE
available_boxes = total_boxes - boxes_owned
