from dino_runner.components.image_cloud import Clouds

import random
class Cloud_man:
    def __init__(self):
        self.cloud=[]
        self.cloud.append(Clouds())
    def update(self):
        if len(self.cloud)==0:
            self.cloud.append(Clouds())
        for cloud in self.cloud:
            if cloud.rect.x< -cloud.rect.width:
                self.cloud.pop()


    def draw(self,screen):
        for cloud in self.cloud:
            cloud.draw(screen)


