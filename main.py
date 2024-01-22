import sys
from sidebar import Shapes, Preview, Stats, Score
from tetris import Tetris
from snake import Snake
from settings import *


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_CAPTION)
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.shapes = Shapes()
        self.stats = Stats()
        self.tetris = Tetris(self.stats, self.shapes)
        self.preview = Preview(self.shapes)
        self.score = Score(self.stats)
        self.snake = Snake(self.stats)

    def run(self):
        while True:
            if not self.tetris.is_running or not self.snake.is_running:
                self.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
                self.exit()
            self.display_surface.fill(BACKGROUND_COLOR)
            self.tetris.run()
            self.preview.draw()
            self.score.draw()
            self.snake.run()
            pygame.display.update()
            self.clock.tick(FPS)

    def exit(self):
        pygame.quit()
        self.stats.print()
        sys.exit()


if __name__ == "__main__":
    Main().run()
