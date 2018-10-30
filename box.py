class Box:
    boxes = 0
    owned = 0

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = [0, 0, 0, 0]
        self.closed = 0
        self.owned = None

        Box.boxes += 1

    def __str__(self):
        return f"Box coordinates ({self.x, self.y})"

    def getScore(self):
        return sum(self.walls)

    def displayOwner(self, canvas, offset, gap):
        (x, y) = [point*gap+offset for point in [
            self.x, self.y]]
        if self.owned != None:
            initials = self.owned[:3]
        else:
            initials = ''

        canvas.create_text(x + 25, y + 25, text=initials)
