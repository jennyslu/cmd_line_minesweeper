from square import Square
import random

class Grid(object):
    """docstring for grid."""
    def __init__(self, mines):
        self.size = 8
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
        print '''
        |_____|__0__|__1__|__2__|__3__|__4__|__5__|__6__|__7__|'''

        print_row = '''
        |__{}__|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |'''

        for row in self.grid:
            prow = []
            prow.append(row[0].row)
            for square in row:
                if square.mine:
                    prow.append("*")
                else:
                    prow.append(square.number)
            trow = tuple(prow)
            print print_row.format(*trow)

    def print_grid(self):
        print '''
        |_____|__0__|__1__|__2__|__3__|__4__|__5__|__6__|__7__|'''

        print_row = '''
        |__{}__|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |'''

        for row in self.grid:
            prow = []
            prow.append(row[0].row)
            for square in row:
                if square.display:
                    if square._flagged:
                        prow.append("f")
                    else:
                        prow.append(square.number)
                else:
                    prow.append(" ")
            trow = tuple(prow)
            print print_row.format(*trow)

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
