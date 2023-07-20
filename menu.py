import pygame
from const import *

class Label:
    def __init__(self, pos, text, font):
        self.pos = pos
        self.text = text
        self.font: pygame.font.Font = font

        self.text_img = self.font.render(self.text, False, WHITE).convert_alpha()
        self.rect = self.text_img.get_rect(center = self.pos)
    
    def update(self):
        pass

    def render(self, surf: pygame.Surface):
        surf.blit(self.text_img, self.rect)

class Button:
    def __init__(self, pos, text, font, game_func=None):
        self.pos = pos
        self.text = text
        self.font: pygame.font.Font = font
        self.func = game_func

        self.btn_img = self.font.render(self.text, False, WHITE).convert_alpha()
        self.scaled_btn_img = pygame.transform.scale(self.btn_img, (round(self.btn_img.get_width()*1.25), round(self.btn_img.get_height()*1.25)))
        self.rect = self.btn_img.get_rect(center = self.pos)

        self.img = self.btn_img
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.img = self.scaled_btn_img
            self.rect = self.img.get_rect(center = self.rect.center)
            if pygame.mouse.get_pressed()[0]:
                self.func()
        else:
            self.img = self.btn_img
            self.rect = self.img.get_rect(center = self.rect.center)
    
    def update(self):
        if self.check_click():
            self.game.quit()
    
    def render(self, surf):
        surf.blit(self.img, self.rect)

class GameMenu:
    def __init__(self, game):
        self.game = game
        self.big_font = pygame.font.Font('data/font/font.ttf', 128)
        self.small_font = pygame.font.Font('data/font/font.ttf', 64)
        self.tiny_font = pygame.font.Font('data/font/font.ttf', 32)
        self.label = []
        self.btn = []

        self.init_label()
        self.init_btn()
    
    def init_label(self):
        self.label.append(Label(LABEL_NAME_POS, 'PvZ', self.big_font))
        self.label.append(Label(LABEL_LEVEL_POS, str(self.game.current_level), self.tiny_font))
    
    def clear_label(self):
        self.label.clear()
    
    def init_btn(self):
        self.btn.append(Button(BUTTON_PLAY_POS, 'Play', self.small_font, self.game.quit))
        self.btn.append(Button(BUTTON_DOCS_POS, 'Docs', self.small_font, self.game.quit))
        self.btn.append(Button(BUTTON_QUIT_POS, 'Quit', self.small_font, self.game.quit))
    
    def update(self):
        for btn in self.btn:
            btn.update()

    def render(self, surf):
        for label in self.label:
            label.render(surf)
        for btn in self.btn:
            btn.render(surf)
