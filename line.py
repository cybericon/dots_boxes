from box import Box
from config import BOXES, players, available_boxes, total_boxes, boxes_owned, playerOne, playerTwo


class Line:
    def __init__(self, points, frame):
        self.frame = frame
        self.x1, self.y1, self.x2, self.y2 = points
        self.canvas = frame.canvas
        self.scoreboard = frame.scoreboard

    def drawLine(self, canvas, offset, gap):
        (x, y, a, b) = [point*gap+offset for point in [
            self.x1, self.y1, self.x2, self.y2]]
        line = canvas.create_line(x, y, a, b, fill="#dddddd", width=2)
        canvas.tag_bind(line, "<Button-1>", lambda event,
                        line=line, canvas=canvas: self.selectLine(line, canvas))

    def selectLine(self, line_object, canvas):
        global players
        canvas.itemconfig(line_object, fill=players[0].color)
        self.updateBoxes(BOXES)

    def updateBoxes(self, boxes):
        pass

    def updateScore(self):
        self.frame.scoreboard.create_rectangle(
            0, 0, 230, 600, fill=self.frame._dark_bg
        )
        self.frame.createHeading(10, text="Boxes")
        self.frame.createBoxInfo(50,
                                 text="Available Boxes \t ", attach_variable=available_boxes())
        self.frame.createBoxInfo(70,
                                 text="Owned Boxes \t ", attach_variable=boxes_owned())
        # Second Block
        self.frame.createHeading(140, text="Boxes Owned")
        self.frame.createBoxInfo(180,
                                 text=f"{playerOne.name} \t \t ", attach_variable=playerOne.owned)
        self.frame.createBoxInfo(200,
                                 text=f"{playerTwo.name} \t \t ", attach_variable=playerTwo.owned)
        # Third Block
        self.frame.createHeading(270, text="Current Move", color="#bdccd4")
        self.frame.createBoxInfo(310,
                                 text=f"{players[0].name}", color="#ff931e", attach_variable='')
        if boxes_owned() == total_boxes:
            winner = playerOne if playerOne.owned > playerTwo.owned else playerTwo
            self.frame.createHeading(
                400, text=f"{winner.name} Wins")


class VerticalLine(Line):

    def __init__(self, points, frame):
        Line.__init__(self, points, frame)

    def updateBoxes(self, boxes):
        global players
        if self.x1 > 0 and self.x1 < len(boxes[0]):
            box1 = boxes[self.y1][self.x1]
            box1.walls[3] = 1
            box2 = boxes[self.y1][self.x1 - 1]
            box2.walls[1] = 1

            if box1.getScore() == 4 and box2.getScore() == 4:
                box1.owned = players[0].name
                players[0].owned += 1
                box1.displayOwner(self.canvas, 100, 50)
                box2.owned = players[0].name
                players[0].owned += 1
                box2.displayOwner(self.canvas, 100, 50)
            elif box1.getScore() == 4:
                box1.owned = players[0].name
                players[0].owned += 1
                box1.displayOwner(self.canvas, 100, 50)
            elif box2.getScore() == 4:
                box2.owned = players[0].name
                players[0].owned += 1
                box2.displayOwner(self.canvas, 100, 50)
            else:
                p1, p2 = players
                players = [p2, p1]

        if self.x1 == 0:
            box = boxes[self.y1][self.x1]
            box.walls[3] = 1
            if box.getScore() == 4:
                box.owned = players[0].name
                players[0].owned += 1
                box.displayOwner(self.canvas, 100, 50)
            else:
                p1, p2 = players
                players = [p2, p1]

        if self.x1 == len(boxes[0]):
            box = boxes[self.y1][self.x1 - 1]
            box.walls[1] = 1
            if box.getScore() == 4:
                box.owned = players[0].name
                players[0].owned += 1
                box.displayOwner(self.canvas, 100, 50)
            else:
                p1, p2 = players
                players = [p2, p1]
        self.updateScore()


class HorizontalLine(Line):
    def __init__(self, points, frame):
        Line.__init__(self, points, frame)

    def updateBoxes(self, boxes):
        global players
        if self.y1 > 0 and self.y1 < len(boxes[0]):
            box1 = boxes[self.y1][self.x1]
            box1.walls[0] = 1
            box2 = boxes[self.y1 - 1][self.x1]
            box2.walls[2] = 1
            if box1.getScore() == 4 and box2.getScore() == 4:
                box1.owned = players[0].name
                players[0].owned += 1
                box1.displayOwner(self.canvas, 100, 50)
                box2.owned = players[0].name
                players[0].owned += 1
                box2.displayOwner(self.canvas, 100, 50)
            elif box1.getScore() == 4:
                box1.owned = players[0].name
                players[0].owned += 1
                box1.displayOwner(self.canvas, 100, 50)
            elif box2.getScore() == 4:
                box2.owned = players[0].name
                players[0].owned += 1
                box2.displayOwner(self.canvas, 100, 50)
            else:
                p1, p2 = players
                players = [p2, p1]

        if self.y1 == 0:
            box = boxes[self.y1][self.x1]
            box.walls[0] = 1
            if box.getScore() == 4:
                box.owned = players[0].name
                players[0].owned += 1
                box.displayOwner(self.canvas, 100, 50)
            else:
                p1, p2 = players
                players = [p2, p1]

        if self.y1 == len(boxes[0]):
            box = boxes[self.y1 - 1][self.x1]
            box.walls[2] = 1
            if box.getScore() == 4:
                box.owned = players[0].name
                players[0].owned += 1
                box.displayOwner(self.canvas, 100, 50)
            else:
                p1, p2 = players
                players = [p2, p1]
        self.updateScore()
