import pygame

FPS = 60

CELL_SIZE = 40
PADDING = 20

TETRIS_ROWS = 20
TETRIS_COLS = 10
TETRIS_WIDTH = TETRIS_COLS * CELL_SIZE
TETRIS_HEIGHT = TETRIS_ROWS * CELL_SIZE
TETRIS_UPDATE_SPEED = 200
TETRIS_UPDATE_SPEED_EXTRA = TETRIS_UPDATE_SPEED * 0.3
TETRIS_MOVE_WAIT_TIME = TETRIS_UPDATE_SPEED
TETRIS_ROTATE_WAIT_TIME = TETRIS_UPDATE_SPEED
TETRIS_ROW_POINTS = 10
TETRIS_BLOCK_OFFSET = pygame.Vector2(TETRIS_COLS // 2, -1)
TETRIS_SHAPES = {
    "T": {"shape": [(0, 0), (-1, 0), (1, 0), (0, -1)], "color": "#7b217f"},
    "O": {"shape": [(0, 0), (0, -1), (1, 0), (1, -1)], "color": "#f1e60d"},
    "J": {"shape": [(0, 0), (0, -1), (0, 1), (-1, 1)], "color": "#204b9b"},
    "L": {"shape": [(0, 0), (0, -1), (0, 1), (1, 1)], "color": "#f07e13"},
    "I": {"shape": [(0, 0), (0, -1), (0, -2), (0, 1)], "color": "#6cc6d9"},
    "S": {"shape": [(0, 0), (-1, 0), (0, -1), (1, -1)], "color": "#65b32e"},
    "Z": {"shape": [(0, 0), (1, 0), (0, -1), (-1, -1)], "color": "#e51b20"},
}

SNAKE_ROWS = TETRIS_ROWS
SNAKE_COLS = 20
SNAKE_WIDTH = SNAKE_COLS * CELL_SIZE
SNAKE_HEIGHT = TETRIS_HEIGHT
SNAKE_UPDATE_SPEED = TETRIS_UPDATE_SPEED
SNAKE_BODY_COLOR = "#36ab45"
SNAKE_APPLE_COLOR = "#cc0033"
SNAKE_APPLE_POINTS = 1
SNAKE_START_LENGTH = 3
SNAKE_START_ROW = SNAKE_ROWS // 2
SNAKE_START_COL = SNAKE_START_LENGTH + 2

SIDEBAR_WIDTH = 200
SIDEBAR_PREVIEW_FRACTION = 0.7
SIDEBAR_SCORE_FRACTION = 1 - SIDEBAR_PREVIEW_FRACTION

WINDOW_WIDTH = TETRIS_WIDTH + SIDEBAR_WIDTH + SNAKE_WIDTH + PADDING * 4
WINDOW_HEIGHT = TETRIS_HEIGHT + PADDING * 2
WINDOW_CAPTION = "Tetrisnake"

HISTORY_FILE = "history.json"

BACKGROUND_COLOR = "#24292d"

FONT_SIZE = 30
FONT_COLOR = "#d2d7db"

GRID_COLOR = FONT_COLOR
GRID_WIDTH = 1
GRID_OPACITY = 50

BORDER_COLOR = FONT_COLOR
BORDER_WIDTH = 3
