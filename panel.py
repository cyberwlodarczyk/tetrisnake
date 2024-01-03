from settings import *


class Panel:
    def __init__(self, size, **kwargs):
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect(**kwargs)

    def draw_background(self):
        self.surface.fill(BACKGROUND_COLOR)

    def draw_border(self):
        pygame.draw.rect(
            self.display_surface, BORDER_COLOR, self.rect, BORDER_WIDTH, BORDER_RADIUS
        )

    def draw(self):
        self.display_surface.blit(self.surface, self.rect)
