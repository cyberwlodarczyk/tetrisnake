import sys
from shared import Grid, Panel, Timer
from sidebar import Shapes, Stats
from settings import *


class Tetris(Panel):
    def __init__(self, stats: Stats, shapes: Shapes):
        super().__init__((TETRIS_WIDTH, TETRIS_HEIGHT), topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()
        self.stats = stats
        self.shapes = shapes
        self.grid = Grid(self.surface, TETRIS_ROWS, TETRIS_COLS)
        self.current_score = 0
        self.current_lines = 0
        self.cells = [[0 for _ in range(TETRIS_COLS)] for _ in range(TETRIS_ROWS)]
        self.tetromino = None
        self.create_tetromino()
        self.down_speed = TETRIS_UPDATE_SPEED
        self.down_speed_faster = self.down_speed * 0.3
        self.down_pressed = False
        self.timers = {
            "vertical move": Timer(self.down_speed, True, self.move_down),
            "horizontal move": Timer(TETRIS_MOVE_WAIT_TIME),
            "rotate": Timer(TETRIS_ROTATE_WAIT_TIME),
        }
        for timer in self.timers.values():
            timer.start()

    def check_game_over(self):
        if self.tetromino:
            for block in self.tetromino.blocks:
                if block.pos.y < 0:
                    pygame.quit()
                    sys.exit()

    def check_finished_rows(self):
        delete_rows = [i for i, row in enumerate(self.cells) if all(row)]
        if delete_rows:
            for delete_row in delete_rows:
                for block in self.cells[delete_row]:
                    block.kill()
                for row in self.cells:
                    for block in row:
                        if block and block.pos.y < delete_row:
                            block.pos.y += 1
            self.cells = [[0 for _ in range(TETRIS_COLS)] for _ in range(TETRIS_ROWS)]
            for block in self.sprites:
                self.cells[int(block.pos.y)][int(block.pos.x)] = block
            self.stats.increment_lines(len(delete_rows))

    def create_tetromino(self):
        self.check_game_over()
        self.check_finished_rows()
        self.tetromino = Tetromino(
            self.sprites,
            self.cells,
            self.shapes.get_next(),
        )

    def update_timer(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):
        if not self.tetromino.move_down():
            self.create_tetromino()

    def get_input(self):
        keys = pygame.key.get_pressed()
        if not self.timers["horizontal move"].is_running:
            if keys[pygame.K_a]:
                self.tetromino.move_horizontal(-1)
                self.timers["horizontal move"].start()
            if keys[pygame.K_d]:
                self.tetromino.move_horizontal(1)
                self.timers["horizontal move"].start()
        if not self.timers["rotate"].is_running:
            if keys[pygame.K_w]:
                self.tetromino.rotate()
                self.timers["rotate"].start()
        if not self.down_pressed and keys[pygame.K_s]:
            self.down_pressed = True
            self.timers["vertical move"].duration = self.down_speed_faster
        if self.down_pressed and not keys[pygame.K_s]:
            self.down_pressed = False
            self.timers["vertical move"].duration = self.down_speed

    def draw(self):
        super().draw_background()
        self.sprites.draw(self.surface)
        self.grid.draw()
        super().draw()
        super().draw_border()

    def run(self):
        self.get_input()
        self.update_timer()
        self.sprites.update()
        self.draw()


class Tetromino:
    def __init__(self, group, cells, shape):
        self.cells = cells
        self.shape = shape
        self.blocks = [
            Block(group, cells, pos, TETROMINOS[shape]["color"])
            for pos in TETROMINOS[shape]["shape"]
        ]

    def move_horizontal(self, amount):
        collisions = [
            block.is_horizontal_collision(int(block.pos.x + amount))
            for block in self.blocks
        ]
        if not any(collisions):
            for block in self.blocks:
                block.pos.x += amount
            return True

    def move_down(self):
        collisions = [
            block.is_vertical_collision(int(block.pos.y + 1)) for block in self.blocks
        ]
        if not any(collisions):
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


class Block(pygame.sprite.Sprite):
    def __init__(self, group, cells, pos, color):
        super().__init__(group)
        self.cells = cells
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)
        self.pos = pygame.Vector2(pos) + TETRIS_BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft=self.pos * CELL_SIZE)

    def is_horizontal_collision(self, x):
        if not 0 <= x < TETRIS_COLS:
            return True
        if self.cells[int(self.pos.y)][x]:
            return True

    def is_vertical_collision(self, y):
        if not y < TETRIS_ROWS:
            return True
        if self.cells[y][int(self.pos.x)] and y >= 0:
            return True

    def rotate(self, pivot_pos):
        return pivot_pos + (self.pos - pivot_pos).rotate(90)

    def update(self):
        self.rect.topleft = self.pos * CELL_SIZE