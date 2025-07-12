import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):

    def __init__(self):
        # Choose randomly between a large or small cactus type
        if random.randint(0, 1) == 0:
            # It's a large cactus
            image_list = LARGE_CACTUS
            y_pos = 300
        else:
            # It's a small cactus
            image_list = SMALL_CACTUS
            y_pos = 325
        
        # Select a random image from the chosen list and call the parent constructor
        super().__init__(random.choice(image_list))
        self.rect.y = y_pos