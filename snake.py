import sys
import random
from shared import Grid, Panel, Timer
from sidebar import Stats
from settings import *


def random_pos():
    return (
        pygame.Vector2(
            random.randint(0, SNAKE_COLS - 1), random.randint(0, SNAKE_ROWS - 1)
        )
        * CELL_SIZE
    )


class Snake(Panel):
    def __init__(self, stats: Stats):
        super().__init__(
            (SNAKE_WIDTH, SNAKE_HEIGHT),
            topright=(WINDOW_WIDTH - PADDING, PADDING),
        )
        self.stats = stats
        self.grid = Grid(self.surface, SNAKE_ROWS, SNAKE_COLS)
        self.body = [
            pygame.Vector2(SNAKE_START_COL - col, SNAKE_START_ROW) * CELL_SIZE
            for col in range(SNAKE_START_LENGTH)
        ]
        self.direction = pygame.Vector2(1, 0)
        self.set_apple_pos()
        self.timer = Timer(
            SNAKE_UPDATE_SPEED,
            True,
            self.update,
        )
        self.timer.start()

    def set_apple_pos(self):
        while True:
            self.apple = random_pos()
            if self.apple not in self.body:
                break

    def get_input(self):
        keys = pygame.key.get_pressed()
        x, y = 0, 0
        if keys[pygame.K_UP]:
            if self.direction.y != 1:
                x, y = 0, -1
        if keys[pygame.K_RIGHT]:
            if self.direction.x != -1:
                x, y = 1, 0
        if keys[pygame.K_LEFT]:
            if self.direction.x != 1:
                x, y = -1, 0
        if keys[pygame.K_DOWN]:
            if self.direction.y != -1:
                x, y = 0, 1
        if x != 0 or y != 0:
            self.direction = pygame.Vector2(x, y)

    def draw_cell(self, point, color):
        rect = pygame.Rect(point.x, point.y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.surface, color, rect)

    def draw(self):
        super().draw_background()
        for point in self.body:
            self.draw_cell(point, SNAKE_BODY_COLOR)
        self.draw_cell(self.apple, SNAKE_APPLE_COLOR)
        self.grid.draw()
        super().draw()
        super().draw_border()

    def update(self):
        self.body.insert(0, self.body[0] + self.direction * CELL_SIZE)
        if not self.body[0] == self.apple:
            self.body.pop()
        else:
            self.stats.increment_apples()
            self.set_apple_pos()
        if (
            self.body[0] in self.body[1:]
            or not 0 <= self.body[0].x < SNAKE_WIDTH
            or not 0 <= self.body[0].y < SNAKE_HEIGHT
        ):
            pygame.quit()
            sys.exit()

    def run(self):
        self.get_input()
        self.timer.update()
        self.draw()
