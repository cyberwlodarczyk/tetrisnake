import os
import random
from shared import Panel
from settings import *


def random_shape():
    return random.choice(list(TETROMINOS.keys()))


class Shapes:
    def __init__(self) -> None:
        self.queue = [random_shape() for _ in range(3)]

    def get_next(self):
        self.queue.append(random_shape())
        return self.queue.pop(0)


class Preview(Panel):
    def __init__(self, shapes: Shapes):
        super().__init__(
            (SIDEBAR_WIDTH, TETRIS_HEIGHT * PREVIEW_HEIGHT_FRACTION),
            topleft=((TETRIS_WIDTH + PADDING * 2, PADDING)),
        )
        self.shapes = shapes
        self.surfaces = {
            shape: pygame.image.load(
                os.path.join("assets", f"{shape}.png")
            ).convert_alpha()
            for shape in TETROMINOS.keys()
        }
        self.increment_height = self.surface.get_height() / 3

    def draw_shapes(self):
        for i, shape in enumerate(self.shapes.queue):
            surface = self.surfaces[shape]
            x = self.surface.get_width() // 2
            y = self.increment_height / 2 + i * self.increment_height
            self.surface.blit(
                surface,
                surface.get_rect(center=(x, y)),
            )

    def draw(self):
        super().draw_background()
        self.draw_shapes()
        super().draw()
        super().draw_border()


class Stats:
    def __init__(self):
        self.score = 0
        self.lines = 0
        self.apples = 0

    def get_labels(self) -> list[tuple[str, int]]:
        return [
            ("Score", self.score),
            ("Lines", self.lines),
            ("Apples", self.apples),
        ]

    def increment_lines(self, count: int):
        self.score += count * 10
        self.lines += count

    def increment_apples(self):
        self.score += 1
        self.apples += 1


class Score(Panel):
    def __init__(self, stats: Stats):
        super().__init__(
            (SIDEBAR_WIDTH, TETRIS_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING),
            bottomleft=(TETRIS_WIDTH + PADDING * 2, WINDOW_HEIGHT - PADDING),
        )
        self.stats = stats
        self.font = pygame.font.Font(os.path.join("assets", "Russo_One.ttf"), FONT_SIZE)
        self.increment_height = self.surface.get_height() / 3

    def draw_text(self):
        for i, text in enumerate(self.stats.get_labels()):
            x = self.surface.get_width() // 2
            y = self.increment_height / 2 + i * self.increment_height
            text_surface = self.font.render(f"{text[0]}: {text[1]}", True, FONT_COLOR)
            text_rect = text_surface.get_rect(center=(x, y))
            self.surface.blit(text_surface, text_rect)

    def draw(self):
        super().draw_background()
        self.draw_text()
        super().draw()
        super().draw_border()
