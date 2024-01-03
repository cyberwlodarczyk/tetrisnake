from settings import *
from os import path

from panel import Panel


class Score(Panel):
    def __init__(self):
        super().__init__(
            (SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING),
            bottomright=(WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING),
        )
        self.font = pygame.font.Font(path.join("assets", "Russo_One.ttf"), 30)
        self.increment_height = self.surface.get_height() / 3

        self.score = 0
        self.level = 1
        self.lines = 0

    def draw_text(self):
        for i, text in enumerate(
            [("Score", self.score), ("Level", self.level), ("Lines", self.lines)]
        ):
            x = self.surface.get_width() // 2
            y = self.increment_height / 2 + i * self.increment_height
            text_surface = self.font.render(f"{text[0]}: {text[1]}", True, "white")
            text_rect = text_surface.get_rect(center=(x, y))
            self.surface.blit(text_surface, text_rect)

    def draw(self):
        super().draw_background()
        self.draw_text()
        super().draw()
        super().draw_border()
