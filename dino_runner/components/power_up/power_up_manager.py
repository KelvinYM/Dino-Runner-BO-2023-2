from dino_runner.components.power_up.shield import Shield
class PowerUpManager:
    def __init__(self):
        self.power_ups=[]
    def update(self,game_speed,points,player):
        if len(self.power_ups)==0 and points %200==0:
            self.power_ups.append(Shield())
        for power_up  in self.power_ups:
            if power_up.used or power_up.rect.x<-power_up.rect.width:
                self.power_ups.pop()
            power_up.update(game_speed,player)
    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)