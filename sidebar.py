import os
import random
from shared import Panel
from settings import *


def random_shape():
    return random.choice(list(TETRIS_SHAPES.keys()))


class Shapes:
    def __init__(self) -> None:
        self.queue = [random_shape() for _ in range(3)]

    def get_next(self):
        self.queue.append(random_shape())
        return self.queue.pop(0)


class Preview(Panel):
    def __init__(self, shapes: Shapes):
        super().__init__(
            (SIDEBAR_WIDTH, TETRIS_HEIGHT * SIDEBAR_PREVIEW_FRACTION),
            topleft=((TETRIS_WIDTH + PADDING * 2, PADDING)),
        )
        self.shapes = shapes
        self.surfaces = {
            shape: pygame.image.load(
                os.path.join("assets", f"{shape}.png")
            ).convert_alpha()
            for shape in TETRIS_SHAPES.keys()
        }

    def draw_shapes(self):
        width, height = self.surface.get_size()
        for i, shape in enumerate(self.shapes.queue):
            surface = self.surfaces[shape]
            x = width // 2
            y = height // 6 + i * height // 3
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
        self.rows = 0
        self.apples = 0

    def get_labels(self) -> list[tuple[str, int]]:
        return [
            ("Score", self.score),
            ("Rows", self.rows),
            ("Apples", self.apples),
        ]

    def print(self):
        print(f"{self.score} points scored")
        print(f"{self.rows} tetris rows filled")
        print(f"{self.apples} snake apples eaten")

    def increment_rows(self, count: int):
        self.score += count * TETRIS_ROW_POINTS
        self.rows += count

    def increment_apples(self):
        self.score += SNAKE_APPLE_POINTS
        self.apples += 1


class Score(Panel):
    def __init__(self, stats: Stats):
        super().__init__(
            (SIDEBAR_WIDTH, TETRIS_HEIGHT * SIDEBAR_SCORE_FRACTION - PADDING),
            bottomleft=(TETRIS_WIDTH + PADDING * 2, WINDOW_HEIGHT - PADDING),
        )
        self.stats = stats
        self.font = pygame.font.Font(os.path.join("assets", "Russo_One.ttf"), FONT_SIZE)

    def draw_text(self):
        width, height = self.surface.get_size()
        for i, text in enumerate(self.stats.get_labels()):
            x = width // 2
            y = height // 6 + i * height // 3
            text_surface = self.font.render(f"{text[0]}: {text[1]}", True, FONT_COLOR)
            text_rect = text_surface.get_rect(center=(x, y))
            self.surface.blit(text_surface, text_rect)

    def draw(self):
        super().draw_background()
        self.draw_text()
        super().draw()
        super().draw_border()
