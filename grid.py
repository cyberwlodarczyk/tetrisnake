from settings import *


class Grid:
    def __init__(self, display_surface, rows, cols):
        self.display_surface = display_surface
        self.rows = rows
        self.cols = cols
        self.surface = display_surface.copy()
        self.surface.fill((0, 0, 0))
        self.surface.set_colorkey((0, 0, 0))
        self.surface.set_alpha(GRID_OPACITY)

    def draw(self):
        for col in range(1, self.cols):
            x = col * CELL_SIZE
            pygame.draw.line(
                self.surface,
                GRID_COLOR,
                (x, 0),
                (x, self.surface.get_height()),
                GRID_WIDTH,
            )
        for row in range(1, self.rows):
            y = row * CELL_SIZE
            pygame.draw.line(
                self.surface,
                GRID_COLOR,
                (0, y),
                (self.surface.get_width(), y),
                GRID_WIDTH,
            )
        self.display_surface.blit(self.surface, (0, 0))
