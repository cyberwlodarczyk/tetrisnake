from settings import *
from sys import exit

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

        # Components
        self.game = Game()
        self.preview = Preview()
        self.score = Score()

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
            self.preview.run()
            self.score.run()

            # Updating the game
            pygame.display.update()
            self.clock.tick()


if __name__ == "__main__":
    main = Main()
    main.run()
