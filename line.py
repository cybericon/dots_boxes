from box import Box
from config import BOXES


class Line:
    def __init__(self, points, canvas):
        self.x1, self.y1, self.x2, self.y2 = points
        self.canvas = canvas

    def drawLine(self, canvas, offset, gap):
        (x, y, a, b) = [point*gap+offset for point in [
            self.x1, self.y1, self.x2, self.y2]]
        line = canvas.create_line(x, y, a, b, fill="#dddddd", width=2)
        canvas.tag_bind(line, "<Button-1>", lambda event,
                        line=line, canvas=canvas: self.selectLine(line, canvas))

    def selectLine(self, line_object, canvas):
        canvas.itemconfig(line_object, fill='#ff931e')
        self.updateBoxes(BOXES)
        # updating box and score is yet to implement

    def updateBoxes(self, boxes):
        pass


class VerticalLine(Line):
    def __init__(self, points, canvas):
        Line.__init__(self, points, canvas)

    def updateBoxes(self, boxes):
        if self.x1 > 0 and self.x1 < len(boxes[0]):
            box1 = boxes[self.y1][self.x1]
            box1.walls[3] = 1
            box2 = boxes[self.y1][self.x1 - 1]
            box2.walls[1] = 1
            box1.displayScore(self.canvas, 100, 50)
            box2.displayScore(self.canvas, 100, 50)
        if self.x1 == 0:
            box = boxes[self.y1][self.x1]
            box.walls[3] = 1
            box.displayScore(self.canvas, 100, 50)
        if self.x1 == len(boxes[0]):
            box = boxes[self.y1][self.x1 - 1]
            box.walls[1] = 1
            box.displayScore(self.canvas, 100, 50)


class HorizontalLine(Line):
    def __init__(self, points, canvas):
        Line.__init__(self, points, canvas)

    def updateBoxes(self, boxes):
        if self.y1 > 0 and self.y1 < len(boxes[0]):
            box1 = boxes[self.y1][self.x1]
            box1.walls[0] = 1
            box2 = boxes[self.y1 - 1][self.x1]
            box2.walls[2] = 1
            box1.displayScore(self.canvas, 100, 50)
            box2.displayScore(self.canvas, 100, 50)
        if self.y1 == 0:
            box = boxes[self.y1][self.x1]
            box.walls[0] = 1
            box.displayScore(self.canvas, 100, 50)
        if self.y1 == len(boxes[0]):
            box = boxes[self.y1 - 1][self.x1]
            box.walls[2] = 1
            box.displayScore(self.canvas, 100, 50)
