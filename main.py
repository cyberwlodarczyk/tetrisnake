from random import choice
from sys import exit
from game import Game
from preview import Preview
from score import Score
from snake import Snake
from settings import *


def random_shape():
    return choice(list(TETROMINOS.keys()))


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris")
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.next_shapes = [random_shape() for _ in range(3)]
        self.game = Game(self.get_next_shape, self.update_score)
        self.preview = Preview()
        self.score = Score()
        self.snake = Snake()

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        self.next_shapes.append(random_shape())
        return self.next_shapes.pop(0)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.display_surface.fill(BACKGROUND_COLOR)
            self.game.run()
            self.preview.draw(self.next_shapes)
            self.score.draw()
            self.snake.draw()
            pygame.display.update()
            self.clock.tick()


if __name__ == "__main__":
    Main().run()
