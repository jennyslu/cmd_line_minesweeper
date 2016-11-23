class Square(object):
    """docstring for square."""
    def __init__(self, pos):
        self.row = pos[0]
        self.col = pos[1]
        self._flagged = False
        self.number = 0
        self.mine = False
        self.display = False

    def become_mine(self):
        self.mine = True
        self.number = None

    def count_mines(self):
        self.number += 1

    def clicked(self):
        self.display = True

    def flagged(self):
        self._flagged = True
        self.display = True

    def unflagged(self):
        self._flagged = False
        self.display = False
