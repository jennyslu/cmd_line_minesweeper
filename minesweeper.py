from grid import Grid

class Minesweeper(object):
    """docstring for minesweeper."""
    def __init__(self, size, mines):
        self.over = False
        self.size = size
        self.mines = mines
        self.grid = Grid(self.size, self.mines)

    def play(self):
        # self.grid = Grid(self.size, self.mines)
        self.mine_locs = self.grid.set_mines()
        self.grid.set_numbers()
        self.grid.reveal()
        self.grid.print_grid()
        self.flagged_cells = []
        while not self.over:
            self.click_type = raw_input("Flag or click? F for flag, anything else for click ")
            if self.click_type == "F":
                print "Flag"
                self.chosen = self.ask_position()
                print self.chosen
                if self.chosen in self.flagged_cells:
                    "Unflag cell"
                    self.grid.unflag(self.chosen)
                else:
                    self.flagged_cells.append(self.chosen)
                    "Flag cell"
                    self.grid.flag(self.chosen)
                    #check if you've won
                    if self.flagged_cells == self.mine_locs:
                        print "Check"
                        self.over = True
                        print "You found them all! You win!"
                        self.grid.reveal()
                        return None
            else:
                self.chosen = self.ask_position()
                if self.chosen in self.mine_locs:
                    self.over = True
                    print "BOOM! Game over!"
                    self.grid.reveal()
                    return None
                self.grid.click(self.chosen)
            self.grid.print_grid()

    def ask_position(self):
        row = int(raw_input("Row number? Integers from 0 to 7 valid "))
        col = int(raw_input("Column number? Integers from 0 to 7 valid "))
        return tuple([row, col])


if __name__ == '__main__':
    bigness = int(raw_input("How big of a grid do you want? "))
    difficulty = int(raw_input("Number of mines? "))
    game = Minesweeper(bigness, difficulty)
    game.play()
