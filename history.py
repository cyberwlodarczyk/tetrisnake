import json
from datetime import datetime, timedelta
from sidebar import Stats
from settings import *


class History:
    def __init__(self):
        self.load()
        self.stop()

    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.is_running = True

    def stop(self):
        self.start_time = 0
        self.is_running = False

    def add(self, stats: Stats):
        self.data.append(
            {
                "date": datetime.now().isoformat(),
                "time": str(
                    timedelta(milliseconds=pygame.time.get_ticks() - self.start_time)
                ),
                "score": stats.score,
                "rows": stats.rows,
                "apples": stats.apples,
            }
        )

    def load(self):
        try:
            with open(HISTORY_FILE) as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = []

    def save(self):
        with open(HISTORY_FILE, "w") as f:
            json.dump(self.data, f, indent=2)
