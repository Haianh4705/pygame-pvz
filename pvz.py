import pygame, sys
from const import *
from utils import load_img, load_imgs
from menu import GameMenu
from map import Map

class Pvz:
    ALL_STATE = ['game-menu', 'docs', 'in-game', 'pause']
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('PvZ')

        self.state = 'game-menu'

        self.window = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        self.display = pygame.Surface(DISPLAY_SIZE)

        self.clock = pygame.time.Clock()

        self.assets = {
            'peashooter': load_imgs('single-peashooter'),
            'sunflower': load_imgs('single-sunflower'),
            'normal-zombie': load_img('normal-zombie/1.png'),
            'lawn-mower': load_img('lawn-mower/1.png'),
            'map': load_img('6-lane-map/map.png')
        }

        self.current_world = 1
        self.current_level = 1
        self.level = {}

        self.game_menu = GameMenu(self)
        self.map = Map(self)
    
    def quit(self):
        pygame.quit()
        sys.exit()
    
    def game_menu_state(self):
        self.state = 'game-menu'
        self.game_menu.init_label()
        self.game_menu.init_btn()
    
    def in_game_state(self):
        self.state = 'in-game'
    
    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_menu_state()
            
            self.window.fill(BLACK)
            self.display.fill(BLACK)

            if self.state == 'game-menu':
                self.game_menu.update()
                self.game_menu.render(self.window)
            elif self.state == 'in-game':
                self.map.render(self.display)
                self.window.blit(pygame.transform.scale(self.display, self.window.get_size()), (0, 0))
            
            pygame.display.update()
            pygame.display.set_caption(str(round(self.clock.get_fps(), 1)))

Pvz().run()
