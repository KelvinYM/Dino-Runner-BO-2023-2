from dino_runner.utils.constants import CLOUD
from dino_runner.components.cloud import Cloud
import random 
class Clouds(Cloud):
    Y_POS_CLOUD=150
    def __init__(self):
            image=CLOUD
            super().__init__(image)
            self.rect.y=self.Y_POS_CLOUD
            