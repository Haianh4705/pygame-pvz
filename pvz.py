import pygame, sys
from const import *
from utils import load_img, load_imgs
from menu import GameMenu

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
            'single-shooter': load_imgs('single-shooter')
        }

        self.current_level = '1-1'
        self.level = {}

        self.game_menu = GameMenu(self)
    
    def quit(self):
        pygame.quit()
        sys.exit()
    
    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            
            self.window.fill(BLACK)
            self.display.fill(BLACK)

            if self.state == 'game-menu':
                self.game_menu.update()
                self.game_menu.render(self.window)
            else:
                self.window.blit(pygame.transform.scale(self.display, self.window.get_size()), (0, 0))
            
            pygame.display.update()
            pygame.display.set_caption(str(round(self.clock.get_fps(), 1)))

Pvz().run()
