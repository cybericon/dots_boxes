import core


class Line:
    def __init__(self, points):
        self.x1, self.y1, self.x2, self.y2 = points
        self.boxes = []
        self.walls = []

    def selectLine(self, line_object, canvas):
        canvas.tag_unbind(line_object, "<Button-1>")
        canvas.itemconfig(line_object, fill=core.players[0].color)
        # self.updateBoxes(canvas)
        core.updateMove(self, canvas)


class VerticalLine(Line):

    def __init__(self, points):
        Line.__init__(self, points)
        core.boxes
        if self.x1 > 0 and self.x1 < len(core.boxes[0]):
            self.boxes.append(core.boxes[self.y1][self.x1])
            self.walls.append(3)
            self.boxes.append(core.boxes[self.y1][self.x1 - 1])
            self.walls.append(1)
        if self.x1 == 0:
            self.boxes.append(core.boxes[self.y1][self.x1])
            self.walls.append(3)
        if self.x1 == len(core.boxes[0]):
            self.boxes.append(core.boxes[self.y1][self.x1 - 1])
            self.walls.append(1)


class HorizontalLine(Line):
    def __init__(self, points):
        Line.__init__(self, points)
        core.boxes
        if self.y1 > 0 and self.y1 < len(core.boxes[0]):
            self.boxes.append(core.boxes[self.y1][self.x1])
            self.walls.append(0)
            self.boxes.append(core.boxes[self.y1 - 1][self.x1])
            self.walls.append(2)
        if self.y1 == 0:
            self.boxes.append(core.boxes[self.y1][self.x1])
            self.walls.append(0)
        if self.y1 == len(core.boxes[0]):
            self.boxes.append(core.boxes[self.y1 - 1][self.x1])
            self.walls.append(2)
