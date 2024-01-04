import pygame

FPS = 60

CELL_SIZE = 40

TETRIS_ROWS, TETRIS_COLS = 20, 10
TETRIS_WIDTH, TETRIS_HEIGHT = TETRIS_COLS * CELL_SIZE, TETRIS_ROWS * CELL_SIZE

SNAKE_ROWS, SNAKE_COLS = 20, 20
SNAKE_WIDTH, SNAKE_HEIGHT = SNAKE_COLS * CELL_SIZE, SNAKE_ROWS * CELL_SIZE

SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

PADDING = 20
WINDOW_WIDTH = TETRIS_WIDTH + SIDEBAR_WIDTH + SNAKE_WIDTH + PADDING * 4
WINDOW_HEIGHT = TETRIS_HEIGHT + PADDING * 2

TETRIS_UPDATE_START_SPEED = 200
TETRIS_MOVE_WAIT_TIME = 200
TETRIS_ROTATE_WAIT_TIME = 200
TETRIS_BLOCK_OFFSET = pygame.Vector2(TETRIS_COLS // 2, -1)

SNAKE_UPDATE_START_SPEED = 200
SNAKE_BODY_COLOR = "green"
SNAKE_APPLE_COLOR = "red"

SNAKE_START_LENGTH = 3
SNAKE_START_ROW = SNAKE_ROWS // 2
SNAKE_START_COL = SNAKE_START_LENGTH + 2

BACKGROUND_COLOR = "#1c1c1c"

GRID_WIDTH = 1
GRID_COLOR = "#ffffff"
GRID_OPACITY = 120

BORDER_COLOR = "#ffffff"
BORDER_WIDTH = 2
BORDER_RADIUS = 2

TETROMINOS = {
    "T": {"shape": [(0, 0), (-1, 0), (1, 0), (0, -1)], "color": "#7b217f"},
    "O": {"shape": [(0, 0), (0, -1), (1, 0), (1, -1)], "color": "#f1e60d"},
    "J": {"shape": [(0, 0), (0, -1), (0, 1), (-1, 1)], "color": "#204b9b"},
    "L": {"shape": [(0, 0), (0, -1), (0, 1), (1, 1)], "color": "#f07e13"},
    "I": {"shape": [(0, 0), (0, -1), (0, -2), (0, 1)], "color": "#6cc6d9"},
    "S": {"shape": [(0, 0), (-1, 0), (0, -1), (1, -1)], "color": "#65b32e"},
    "Z": {"shape": [(0, 0), (1, 0), (0, -1), (-1, -1)], "color": "#e51b20"},
}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}
