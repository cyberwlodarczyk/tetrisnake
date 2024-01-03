from settings import *
from pygame.image import load
from os import path

from panel import Panel


class Preview(Panel):
    def __init__(self):
        super().__init__(
            (SIDEBAR_WIDTH, TETRIS_HEIGHT * PREVIEW_HEIGHT_FRACTION),
            topleft=((TETRIS_WIDTH + PADDING * 2, PADDING)),
        )
        self.shape_surfaces = {
            shape: load(path.join("assets", f"{shape}.png")).convert_alpha()
            for shape in TETROMINOS.keys()
        }
        self.increment_height = self.surface.get_height() / 3

    def draw_shapes(self, data):
        for i, shape in enumerate(data):
            shape_surface = self.shape_surfaces[shape]
            x = self.surface.get_width() // 2
            y = self.increment_height / 2 + i * self.increment_height
            self.surface.blit(
                shape_surface,
                shape_surface.get_rect(center=(x, y)),
            )

    def draw(self, shapes):
        super().draw_background()
        self.draw_shapes(shapes)
        super().draw()
        super().draw_border()
