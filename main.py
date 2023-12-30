from settings import *
from sys import exit
from random import choice

# Components
from game import Game
from preview import Preview
from score import Score


class Main:
    def __init__(self):
        # General
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")

        # Shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for _ in range(3)]

        # Components
        self.game = Game(self.get_next_shape, self.update_score)
        self.preview = Preview()
        self.score = Score()

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Display
            self.display_surface.fill(GRAY)

            # Components
            self.game.run()
            self.preview.run(self.next_shapes)
            self.score.run()

            # Updating the game
            pygame.display.update()
            self.clock.tick()


if __name__ == "__main__":
    main = Main()
    main.run()
