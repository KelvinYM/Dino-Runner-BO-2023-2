from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
import random
class ObstacleManager:
    def __init__(self):
        self.obstacles=[]
    def update(self,game_speed,player):
        if len(self.obstacles)==0:
            otype=random.randint(0,1)
            if(otype==0):
                obst=Bird()
            else:
                obst=Cactus()
            self.obstacles.append(obst)
        for obstacle in self.obstacles:
            if obstacle.rect.x< -obstacle.rect.width:
                self.obstacles.pop()
            obstacle.update(game_speed,player)


    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    