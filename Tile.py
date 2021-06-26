class State():
    """ Parent object of Tile. Holds all values nessecary to create a tile """
    # Variables nessecary to give a tile a state
    EMPTY = " "
    HUNGRY = "H"
    THIRSTY = "T"
    SEARCHING_FOR_MATE = "SM"
    SLEEPING = "Z"

    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value
        self.display = " "

class Tile(State):
    """ A class to hold values that a tile may hold """
    def __init__(self, row, column, value):
        super().__init__(row, column, value)


       


