from dino_runner.utils.constants import SMALL_CACTUS,LARGE_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle
import random 
class Cactus(Obstacle):
    Y_POS_CACTUS=330
    Y_POS_LCACTUS=310
    def __init__(self):
        self.type=random.randint(0, 6)
        if self.type<=2:
            image=SMALL_CACTUS[self.type]
            super().__init__(image)
            self.rect.y=self.Y_POS_CACTUS

        else:
            image=LARGE_CACTUS[self.type-6]
            super().__init__(image)
            self.rect.y=self.Y_POS_LCACTUS
            

