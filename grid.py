from square import Square
import random

class Grid(object):
    """docstring for grid."""
    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.grid = [[Square((i,j)) for j in range(self.size)] for i in range(self.size)]

    def set_mines(self):
        mine_locs = []
        while len(mine_locs) < self.mines:
            rand_row = random.randint(0,self.size-1)
            rand_col = random.randint(0,self.size-1)
            if not tuple([rand_row, rand_col]) in mine_locs:
                self.grid[rand_row][rand_col].become_mine()
                mine_locs.append(tuple([rand_row, rand_col]))
        return mine_locs

    def set_numbers(self):
        for row in self.grid:
            for square in row:
                if not square.mine:
                    i = square.row
                    j = square.col
                    surrounding = [(i-1, j-1), (i-1, j), (i-1, j+1),
                                    (i, j-1), (i, j+1),
                                    (i+1, j-1), (i+1, j), (i+1, j+1)]
                    for adjacent in surrounding:
                        try:
                            if self.grid[adjacent[0]][adjacent[1]].mine:
                                self.grid[i][j].count_mines()
                        except IndexError:
                            continue

    def reveal(self):
        top_row = [str(i) for i in range(self.size)]
        ptop = "__|__".join(top_row)
        print "\t|_____|__" + ptop + "__|\n"

        for row in self.grid:
            pcol = "\t|__" + str(row[0].row) + "__|  "
            prow = []
            for square in row:
                if square.mine:
                    prow.append("*")
                else:
                    prow.append(square.number)
            pprow = [str(q) for q in prow]
            trow = tuple(pprow)
            print pcol + "  |  ".join(pprow) + "  |\n"

    def print_grid(self):
        top_row = [str(i) for i in range(self.size)]
        ptop = "__|__".join(top_row)
        print "\t|_____|__" + ptop + "__|\n"

        for row in self.grid:
            pcol = "\t|__" + str(row[0].row) + "__|  "
            prow = []
            for square in row:
                if square.display:
                    if square._flagged:
                        prow.append("F")
                    else:
                        prow.append(square.number)
                else:
                    prow.append(" ")
            pprow = [str(q) for q in prow]
            trow = tuple(pprow)
            print pcol + "  |  ".join(pprow) + "  |\n"

    def click(self, cell):
        i = cell[0]
        j = cell[1]
        self.grid[i][j].clicked()
        if self.grid[i][j].number == 0:
            surrounding = [(i-1, j-1), (i-1, j), (i-1, j+1),
                            (i, j-1), (i, j+1),
                            (i+1, j-1), (i+1, j), (i+1, j+1)]
            for adjacent in surrounding:
                try:
                    if self.grid[adjacent[0]][adjacent[1]].number == 0 and not self.grid[adjacent[0]][adjacent[1]].display:
                        self.click(adjacent)
                except IndexError:
                    continue

    def flag(self, cell):
        i = cell[0]
        j = cell[1]
        self.grid[i][j].flagged()

    def unflag(self, cell):
        i = cell[0]
        j = cell[1]
        self.grid[i][j].unflagged()
