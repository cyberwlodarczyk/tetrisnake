import pygame

FPS = 60

COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

UPDATE_START_SPEED = 200
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2, -1)

BACKGROUND_COLOR = "#1c1c1c"
GRID_COLOR = "#ffffff"

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
