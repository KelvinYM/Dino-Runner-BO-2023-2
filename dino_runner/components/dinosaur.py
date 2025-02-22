import pygame
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DIED
from dino_runner.utils.constants import SHIELD_TYPE,DEFAULT_TYPE
class Dinosaur:

    X_POS=80
    Y_POS=310
    Y_POS_DUCK=340
    Y_POS_JUMP=340
    JUMP_VEL=8.5
    def __init__(self):
        self.image=RUNNING[0]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS
        self.step_index=0
        self.dino_run=True
        self.dino_duck=False
        self.dino_jump=False
        self.jump_vel=self.JUMP_VEL
        self.dino_dead=False
        self.time_up_power_up=False
        self.shield=False
    def run(self):
        self.image=RUNNING[0] if self.step_index<5 else RUNNING[1]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS
        self.step_index+=1
    def duck(self):
        self.image=DUCKING[0] if self.step_index<5 else DUCKING[1]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS_DUCK
        self.step_index+=1
    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run=False
            self.dino_duck=True
            self.dino_jump=False
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run=False
            self.dino_duck=False
            self.dino_jump=True
        elif not self.dino_jump:
            self.dino_run=True
            self.dino_duck=False
            self.dino_jump=False

        if self.step_index>=10:
            self.step_index=0
        if self.shield:
            time_to_show=round((self.time_up_power_up-pygame.time.get_ticks())/1000,2)
            if time_to_show<0:
                self.reset()
    def draw(self,screen):
        if self.dino_dead:
            self.image=DIED
        screen.blit(self.image, self.dino_rect)
        
    def jump(self):
        self.image=JUMPING#[0] if self.step_index<5 else JUMPING[1]
        if self.dino_jump:
            self.dino_rect.y-=self.jump_vel*4
            self.jump_vel-=0.8
        if self.jump_vel<-self.JUMP_VEL:
            self.dino_rect.y=self.Y_POS
            self.dino_jump=False
            self.jump_vel=self.JUMP_VEL
    def set_power_up(self,power_up):
        if power_up.type==SHIELD_TYPE:
            self.type=SHIELD_TYPE
            self.shield=True
            self.time_up_power_up=power_up.time_up
    def reset(self):
        self.type=DEFAULT_TYPE
        self.shield=False
        self.time_up_power_up=0
    