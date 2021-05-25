import pygame
import random
import time
from datetime import datetime
import pygame_menu 

pygame.init()
infoObject = pygame.display.Info()
size = [infoObject.current_w//2,infoObject.current_h*8//9]
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
def show_mode():
    menu.clear()
    menu.add.button('Oasis',start_the_game)
    menu.add.button('Hell')
    menu.add.button('City')
    menu.add.button('Back', back)
    menu.add.button('Quit', pygame_menu.events.EXIT)

def back():
    menu.clear()
    menu.add.button('Select mode', show_mode)
    menu.add.button('Option', show_option)
    menu.add.button('Help')
    menu.add.button('Quit', pygame_menu.events.EXIT)

def help():
    menu.clear()

def show_option():
    menu.clear()
    menu.add.button('Sound')
    menu.add.button('Back', back)
    menu.add.button('Quit',pygame_menu.events.EXIT)
menu_image = pygame_menu.baseimage.BaseImage(image_path='SourceCode/Image/StartImage.png',drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
mytheme = pygame_menu.themes.THEME_ORANGE.copy()
mytheme.background_color = menu_image 
menu = pygame_menu.Menu('MUHIRRYO GOOD', size[0], size[1], theme=mytheme)
menu.add.button('Select mode', show_mode)
menu.add.button('Option',show_option)
menu.add.button('Help')
menu.add.button('Quit',pygame_menu.events.EXIT)
background = pygame.image.load("SourceCode/Image/StartImage.png")
def start_the_game():
    import ChaeKyun
menu.mainloop(screen)