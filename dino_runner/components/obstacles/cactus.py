from dino_runner.utils.constants import SMALL_CACTUS,LARGE_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle
import random 
class Cactus(Obstacle):
    Y_POS_CACTUS=325

    def __init__(self):
        self.type=random.randint(0, 2)
        image=SMALL_CACTUS[self.type]
        super().__init__(image)
        self.rect.y=self.Y_POS_CACTUS
