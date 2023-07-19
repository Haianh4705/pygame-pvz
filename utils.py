import pygame, os

BASE_IMAGE_PATH = 'data/images/'

def load_img(path: str):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_imgs(path: str):
    imgs = []
    for img_name in os.listdir(BASE_IMAGE_PATH + '/' + path):
        imgs.append(load_img(path + '/' + img_name))
    return imgs
