from typing import Callable, Optional
from settings import *


class Grid:
    def __init__(self, display_surface: pygame.Surface, rows: int, cols: int):
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


class Panel:
    def __init__(self, size: tuple[int, int], **kwargs: tuple[int, int]):
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect(**kwargs)

    def draw_background(self):
        self.surface.fill(BACKGROUND_COLOR)

    def draw_border(self):
        pygame.draw.rect(self.display_surface, BORDER_COLOR, self.rect, BORDER_WIDTH)

    def draw(self):
        self.display_surface.blit(self.surface, self.rect)


class Timer:
    def __init__(
        self, duration: int, repeated: bool = False, func: Optional[Callable] = None
    ):
        self.duration = duration
        self.repeated = repeated
        self.func = func
        self.stop()

    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.is_running = True

    def stop(self):
        self.start_time = 0
        self.is_running = False

    def update(self):
        if (
            pygame.time.get_ticks() - self.start_time >= self.duration
            and self.is_running
        ):
            if self.func and self.start_time != 0:
                self.func()
            self.stop()
            if self.repeated:
                self.start()
