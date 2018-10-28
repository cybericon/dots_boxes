class Player:
    """Player class"""

    def __init__(self, name="", color="#2c3e50"):
        self.name = name
        self.owned = 0
        self.color = color

    def move(self):
        pass

    # def move(self, x, y):
    #     # check if x and y are valid points
    #     # check if the line between x and y is valid and not drawn already
    #     # mark the line drawn
    #     # update related boxes

    #     # check if box is complete
    #         # add box to collection
    #         # move again

    #     pass
