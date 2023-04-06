import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud_man import Cloud_man
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_up.power_up_manager import PowerUpManager
from dino_runner.components import text_utils

import random
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player=Dinosaur()
        self.obstacle_manager=ObstacleManager()
        self.power_up_manager=PowerUpManager()
        self.clouds=Cloud_man()
        self.score=0
        self.running=False
        self.death_count=0

    def run(self):
        # Game loop: events - update - draw
        self.running= True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing=False
                pygame.quit()
            if event.type==pygame.KEYDOWN and not self.playing:
                self.playing=True
                self.reset()
    def update(self):
        if self.playing:
            user_input=pygame.key.get_pressed()
            self.player.update(user_input)
            self.obstacle_manager.update(self.game_speed,self.player)
            self.clouds.update()
            self.power_up_manager.update(self.game_speed,self.score,self.player)
            self.score+=1
            if self.player.dino_dead:
                self.playing=False
                self.death_count+=1
        
#actualiza cuando muere
    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.player.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
            self.clouds.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    def draw_score(self):
        score, score_rect=text_utils.get_message("points: "+str(self.score),20,1000,40)
        self.screen.blit(score,score_rect)
        self.game_speed+=0.01
    def draw_menu(self):
        white_color=(255,255,255) 
        self.screen.fill(white_color)
        self.print_menu_element()
    def print_menu_element(self):
        if self.death_count==0:
            text,text_rect=text_utils.get_message("press any key to star",30)
            self.screen.blit(text,text_rect)
        else:
            text,text_rect=text_utils.get_message("press any key to Restar",30)
            score, score_rect=text_utils.get_message('Your Score: '+str(self.score),30,height=SCREEN_HEIGHT//2+50)
            self.screen.blit(text,text_rect)
            self.screen.blit(score,score_rect)
    def reset(self):
        self.game_speed=10
        self.player=Dinosaur()
        self.score=0
        self.obstacle_manager=ObstacleManager()
        self.power_up_manager=PowerUpManager()