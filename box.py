class Box:
    boxes = 0
    owned = 0

    def __init__(self, x, y):
        # self.coordinates = (x, y)
        self.x = x
        self.y = y
        self.walls = [0, 0, 0, 0]
        self.closed = 0
        self.owned = None

        Box.boxes += 1

    def __str__(self):
        return f"Box coordinates ({self.x, self.y})"

    def getScore(self):
        return sum(self.walls)

    def displayScore(self, canvas, offset, gap):
        # return sum(self.walls)
        score = sum(self.walls)
        (x, y) = [point*gap+offset for point in [
            self.x, self.y]]
        canvas.create_oval(x + 5, y + 5, x + 45, y +
                           45, fill='#ecf0f1', outline="")
        canvas.create_text(x + 25, y + 25, text=str(score))

    def displayOwner(self, canvas, offset, gap):
        (x, y) = [point*gap+offset for point in [
            self.x, self.y]]
        canvas.create_oval(x + 5, y + 5, x + 45, y +
                           45, fill='#ecf0f1', outline="")
        canvas.create_text(x + 25, y + 25, text=self.owned[:3])
