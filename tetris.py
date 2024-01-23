from shared import Grid, Panel, Timer
from sidebar import Shapes, Stats
from settings import *


class Block(pygame.sprite.Sprite):
    def __init__(
        self,
        group: pygame.sprite.Group,
        pos: tuple[int, int],
        color: str,
    ):
        super().__init__(group)
        self.pos = pygame.Vector2(pos) + TETRIS_BLOCK_OFFSET
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=self.pos * CELL_SIZE)

    def rotate(self, pivot_pos: pygame.Vector2):
        return pivot_pos + (self.pos - pivot_pos).rotate(90)

    def update(self):
        self.rect.topleft = self.pos * CELL_SIZE


Cells = list[list[Block | None]]


def default_cells() -> Cells:
    return [[None for _ in range(TETRIS_COLS)] for _ in range(TETRIS_ROWS)]


class Tetromino:
    def __init__(self, group: pygame.sprite.Group, cells: Cells, shape: str):
        self.cells = cells
        self.shape = shape
        self.blocks = [
            Block(group, pos, TETRIS_SHAPES[shape]["color"])
            for pos in TETRIS_SHAPES[shape]["shape"]
        ]

    def is_horizontal_collision(self, offset: int):
        for block in self.blocks:
            x = int(block.pos.x + offset)
            if not 0 <= x < TETRIS_COLS:
                return True
            if self.cells[int(block.pos.y)][x]:
                return True

    def is_vertical_collision(self):
        for block in self.blocks:
            y = int(block.pos.y + 1)
            if not y < TETRIS_ROWS:
                return True
            if self.cells[y][int(block.pos.x)] and y >= 0:
                return True

    def move_horizontal(self, offset: int):
        if not self.is_horizontal_collision(offset):
            for block in self.blocks:
                block.pos.x += offset
            return True

    def move_down(self):
        if not self.is_vertical_collision():
            for block in self.blocks:
                block.pos.y += 1
            return True
        else:
            for block in self.blocks:
                self.cells[int(block.pos.y)][int(block.pos.x)] = block

    def rotate(self):
        if self.shape == "O":
            return
        pivot_pos = self.blocks[0].pos
        new_pos = [block.rotate(pivot_pos) for block in self.blocks]
        for pos in new_pos:
            if not 0 <= pos.x < TETRIS_COLS:
                return
            if not pos.y < TETRIS_ROWS:
                return
            if self.cells[int(pos.y)][int(pos.x)]:
                return
        for i, block in enumerate(self.blocks):
            block.pos = new_pos[i]


class Tetris(Panel):
    def __init__(self, stats: Stats, shapes: Shapes):
        super().__init__((TETRIS_WIDTH, TETRIS_HEIGHT), topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()
        self.stats = stats
        self.shapes = shapes
        self.grid = Grid(self.surface, TETRIS_ROWS, TETRIS_COLS)
        self.tetromino = None
        self.is_down_pressed = False
        self.timers = {
            "vertical": Timer(TETRIS_UPDATE_SPEED, True, self.move_down),
            "horizontal": Timer(TETRIS_MOVE_WAIT_TIME),
            "rotational": Timer(TETRIS_ROTATE_WAIT_TIME),
        }
        self.create_cells()
        self.create_tetromino()
        self.stop()

    def start(self):
        self.is_running = True
        for timer in self.timers.values():
            timer.start()

    def stop(self):
        self.is_running = False
        for timer in self.timers.values():
            timer.stop()

    def check_game_over(self):
        if not self.tetromino:
            return
        for block in self.tetromino.blocks:
            if block.pos.y < 0:
                self.stop()

    def check_filled_rows(self):
        if not self.tetromino:
            return
        delete_rows = [i for i, row in enumerate(self.cells) if all(row)]
        if delete_rows:
            for delete_row in delete_rows:
                for block in self.cells[delete_row]:
                    block.kill()
                for row in self.cells:
                    for block in row:
                        if block and block.pos.y < delete_row:
                            block.pos.y += 1
            self.create_cells()
            for block in self.sprites:
                self.cells[int(block.pos.y)][int(block.pos.x)] = block
            self.stats.increment_rows(len(delete_rows))

    def create_cells(self):
        self.cells = default_cells()

    def create_tetromino(self):
        self.check_game_over()
        self.check_filled_rows()
        self.tetromino = Tetromino(
            self.sprites,
            self.cells,
            self.shapes.get_next(),
        )

    def get_input(self):
        keys = pygame.key.get_pressed()
        if not self.timers["horizontal"].is_running:
            if keys[pygame.K_a]:
                self.tetromino.move_horizontal(-1)
                self.timers["horizontal"].start()
            if keys[pygame.K_d]:
                self.tetromino.move_horizontal(1)
                self.timers["horizontal"].start()
        if not self.timers["rotational"].is_running:
            if keys[pygame.K_w]:
                self.tetromino.rotate()
                self.timers["rotational"].start()
        if not self.is_down_pressed and keys[pygame.K_s]:
            self.is_down_pressed = True
            self.timers["vertical"].duration = TETRIS_UPDATE_SPEED_EXTRA
        if self.is_down_pressed and not keys[pygame.K_s]:
            self.is_down_pressed = False
            self.timers["vertical"].duration = TETRIS_UPDATE_SPEED

    def move_down(self):
        if not self.tetromino.move_down():
            self.create_tetromino()

    def draw(self):
        super().draw_background()
        self.sprites.draw(self.surface)
        self.grid.draw()
        super().draw()
        super().draw_border()

    def run(self):
        self.get_input()
        for timer in self.timers.values():
            timer.update()
        self.sprites.update()
        self.draw()
