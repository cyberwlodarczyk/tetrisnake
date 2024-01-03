from pygame.time import get_ticks


class Timer:
    def __init__(self, duration, repeated=False, func=None):
        self.duration = duration
        self.repeated = repeated
        self.func = func
        self.deactivate()

    def activate(self):
        self.start_time = get_ticks()
        self.active = True

    def deactivate(self):
        self.start_time = 0
        self.active = False

    def update(self):
        if get_ticks() - self.start_time >= self.duration and self.active:
            if self.func and self.start_time != 0:
                self.func()
            self.deactivate()
            if self.repeated:
                self.activate()
