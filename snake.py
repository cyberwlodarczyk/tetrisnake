from grid import Grid
from panel import Panel
from settings import *


class Snake(Panel):
    def __init__(self):
        super().__init__(
            (SNAKE_WIDTH, SNAKE_HEIGHT),
            topright=(WINDOW_WIDTH - PADDING, PADDING),
        )
        self.grid = Grid(self.surface, SNAKE_ROWS, SNAKE_COLS)

    def draw(self):
        super().draw_background()
        self.grid.draw()
        super().draw()
        super().draw_border()
